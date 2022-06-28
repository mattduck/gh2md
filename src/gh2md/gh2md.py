#!/usr/bin/env python
# coding: utf-8
import argparse
import datetime
import logging
import os
import pprint
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import requests
from dateutil.parser import parse as dateutil_parse

from . import templates_markdown

ENV_GITHUB_TOKEN = "GITHUB_ACCESS_TOKEN"
GITHUB_ACCESS_TOKEN_PATHS = [
    os.path.expanduser(os.path.join("~", ".config", "gh2md", "token")),
    os.path.expanduser(os.path.join("~", ".github-token")),
]

DESCRIPTION = """Export Github repository issues, pull requests and comments to markdown files:
https://github.com/mattduck/gh2md

Example: gh2md mattduck/gh2md my_issues.md

Credentials are resolved in the following order:

- A `{token}` environment variable.
- An API token stored in ~/.config/gh2md/token or ~/.github-token.

To access private repositories, you'll need a token with the full "repo" oauth
scope.

By default, all issues and pull requests will be fetched. You can disable these
using the --no... flags, eg. --no-closed-prs, or --no-prs.
""".format(
    token=ENV_GITHUB_TOKEN
)

logformat = "[%(asctime)s] [%(levelname)s] %(msg)s"
logging.basicConfig(level=logging.INFO, format=logformat)
logger = logging.getLogger(__name__)


@dataclass
class GithubComment:
    """
    Represents a comment on an issue or PR.
    """

    user_login: str
    user_url: str
    user_avatar_url: str
    created_at: datetime.datetime
    url: str
    body: str


@dataclass
class GithubIssue:
    """
    Represents an Issue or PR. The old Github API used to treat these as a
    single type of object, so initially I'm keeping it that way as we port
    this code to use GraphQL. It might make sense to separate out later.
    """

    user_login: str
    user_url: str
    user_avatar_url: str
    pull_request: bool
    state: str
    body: str
    comments: List[GithubComment]
    number: int
    label_names: List[str]
    title: str
    created_at: datetime.datetime
    url: str


@dataclass
class GithubRepo:
    """
    Root object representing a repo.
    """

    full_name: str
    url: str
    issues: List[GithubIssue]


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "repo",
        help='Github repo to export, in format "owner/repo_name".',
        type=str,
        action="store",
    )
    parser.add_argument(
        "output_path",
        help="Path to write exported issues.",
        type=str,
        action="store",
    )
    parser.add_argument(
        "--multiple-files",
        help="Instead of one file, treat the given path as a directory, and create one file per issue, using a format '{created_at}.{issue_number}.{issue_type}.{issue_state}.md'.",
        action="store_true",
        dest="use_multiple_files",
    )
    parser.add_argument(
        "-I",
        "--idempotent",
        help="Remove non-deterministic values like timestamps. Two runs of gh2md will always produce the same result, as long as the Github data has not changed.",
        action="store_true",
        dest="is_idempotent",
    )
    parser.add_argument(
        "--no-prs",
        help="Don't include pull requests in the export.",
        action="store_false",
        dest="include_prs",
    )
    parser.add_argument(
        "--no-closed-prs",
        help="Don't include closed pull requests in the export.",
        action="store_false",
        dest="include_closed_prs",
    )
    parser.add_argument(
        "--no-issues",
        help="Don't include issues in the export.",
        action="store_false",
        dest="include_issues",
    )
    parser.add_argument(
        "--no-closed-issues",
        help="Don't include closed issues in the export.",
        action="store_false",
        dest="include_closed_issues",
    )
    return parser.parse_args()


@dataclass
class GithubAPI:
    """
    Handles GraphQL API queries.
    """

    token: str = None
    per_page: int = 100

    _ENDPOINT = "https://api.github.com/graphql"
    _REPO_QUERY = """
        query(
          $owner: String!
          $repo: String!
          $issuePerPage: Int!
          $issueNextPageCursor: String
          $pullRequestPerPage: Int!
          $pullRequestNextPageCursor: String
          $issueStates: [IssueState!]
          $pullRequestStates: [PullRequestState!]
        ) {
          rateLimit {
            limit
            cost
            remaining
            resetAt
          }
          repository(owner: $owner, name: $repo) {
            nameWithOwner
            url
            issues(
              first: $issuePerPage
              after: $issueNextPageCursor
              filterBy: { states: $issueStates }
              orderBy: { field: CREATED_AT, direction: DESC }
            ) {
              totalCount
              pageInfo {
                endCursor
                hasNextPage
              }
              nodes {
                id
                number
                url
                title
                body
                state
                createdAt
                author {
                  login
                  url
                  avatarUrl
                }
                labels(first: $issuePerPage) {
                  nodes {
                    name
                    url
                  }
                }
                comments(first: $issuePerPage) {
                  totalCount
                  pageInfo {
                    endCursor
                    hasNextPage
                  }
                  nodes {
                    body
                    createdAt
                    url
                    author {
                      login
                      url
                      avatarUrl
                    }
                  }
                }
              }
            }
            pullRequests(
              first: $pullRequestPerPage
              after: $pullRequestNextPageCursor
              states: $pullRequestStates
              orderBy: { field: CREATED_AT, direction: DESC }
            ) {
              totalCount
              pageInfo {
                endCursor
                hasNextPage
              }
              nodes {
                id
                number
                url
                title
                body
                state
                createdAt
                author {
                  login
                  url
                  avatarUrl
                }
                labels(first: $pullRequestPerPage) {
                  nodes {
                    name
                    url
                  }
                }
                comments(first: $pullRequestPerPage) {
                  totalCount
                  pageInfo {
                    endCursor
                    hasNextPage
                  }
                  nodes {
                    body
                    createdAt
                    url
                    author {
                      login
                      url
                      avatarUrl
                    }
                  }
                }
              }
            }
          }
        }
    """

    _NODE_COMMENT_QUERY = """
        query($perPage: Int!, $id: ID!, $commentCursor: String!) {
          rateLimit {
            limit
            cost
            remaining
            resetAt
          }
          node(id: $id) {
            ... on Issue {
              comments(first: $perPage, after: $commentCursor) {
                totalCount
                pageInfo {
                  endCursor
                  hasNextPage
                }
                nodes {
                  body
                  createdAt
                  url
                  author {
                    login
                    url
                    avatarUrl
                  }
                }
              }
            }
            ... on PullRequest {
              comments(first: $perPage, after: $commentCursor) {
                totalCount
                pageInfo {
                  endCursor
                  hasNextPage
                }
                nodes {
                  body
                  createdAt
                  url
                  author {
                    login
                    url
                    avatarUrl
                  }
                }
              }
            }
          }
        }
    """

    def __post_init__(self):
        self._session = None  # Requests session
        self._total_pages_fetched = 0
        if not self.token:
            logger.warning("No token found. Access to private repositories will fail")

        # For testing
        per_page_override = os.environ.get("_GH2MD_PER_PAGE_OVERRIDE", None)
        if per_page_override:
            self.per_page = int(per_page_override)

    def _request_session(self) -> requests.Session:
        if not self._session:
            self._session = requests.Session()
            self._session.headers.update({"Authorization": "token " + self.token})
        return self._session

    def _post(
        self, json: Dict[str, Any], headers: Optional[Dict[str, Any]] = None
    ) -> Tuple[Dict[str, Any], bool]:
        """
        Make a graphql request and handle errors/retries.
        """
        if headers is None:
            headers = {}
        err = False
        for attempt in range(1, 3):
            try:
                resp = self._request_session().post(
                    self._ENDPOINT, json=json, headers=headers
                )
                resp.raise_for_status()
                err = False
                self._total_pages_fetched += 1
                break
            except Exception:  # Could catch cases that aren't retryable, but I don't think it's too annoying
                err = True
                logger.warning(
                    f"Exception response from request attempt {attempt}", exc_info=True
                )
                time.sleep(3)

        if err:
            decoded = {}
            logger.error("Request failed multiple retries, returning empty data")
        else:
            decoded = resp.json()
            rl = decoded.get("data", {}).get("rateLimit")
            if rl:
                logger.info(
                    f"Rate limit info after request: limit={rl['limit']}, cost={rl['cost']}, remaining={rl['remaining']}, resetAt={rl['resetAt']}"
                )

            errors = decoded.get("errors")
            if errors:
                err = True
                logger.error(f"Found GraphQL errors in response data: {errors}")

        return decoded, err

    def _fetch_repo(
        self,
        owner: str,
        repo: str,
        include_issues: bool,
        include_closed_issues: bool,
        include_prs: bool,
        include_closed_prs: bool,
    ) -> Dict[str, Any]:
        """
        Makes the appropriate number of requests to retrieve all the requested
        issues and PRs.

        Any additional comments beyond the first page in each issue/PR have to
        be fetched separately and merged with the results at the end. This is
        because they live underneath the issue/PR with their own respective
        pagination.
        """

        variables = {
            "owner": owner,
            "repo": repo,
        }
        if include_issues:
            variables["issuePerPage"] = self.per_page
            if not include_closed_issues:
                variables["issueStates"] = ["OPEN"]
        else:
            variables["issuePerPage"] = 0

        if include_prs:
            variables["pullRequestPerPage"] = self.per_page
            if not include_closed_prs:
                variables["pullRequestStates"] = ["OPEN"]
        else:
            variables["pullRequestPerPage"] = 0

        issue_cursor, has_issue_page = None, True
        pr_cursor, has_pr_page = None, True
        success_responses = []
        was_interrupted = False
        while has_issue_page or has_pr_page:
            try:
                # Make the request
                if issue_cursor:
                    variables["issueNextPageCursor"] = issue_cursor
                if pr_cursor:
                    variables["pullRequestNextPageCursor"] = pr_cursor
                data, err = self._post(
                    json={"query": self._REPO_QUERY, "variables": variables}
                )
                if err:
                    break
                else:
                    success_responses.append(data)

                    issues = data["data"]["repository"]["issues"]
                    if issues["nodes"]:
                        issue_cursor = issues["pageInfo"]["endCursor"]
                        has_issue_page = issues["pageInfo"]["hasNextPage"]
                    else:
                        issue_cursor, has_issue_page = None, False

                    prs = data["data"]["repository"]["pullRequests"]
                    if prs["nodes"]:
                        pr_cursor = prs["pageInfo"]["endCursor"]
                        has_pr_page = prs["pageInfo"]["hasNextPage"]
                    else:
                        pr_cursor, has_pr_page = None, False

                    logger.info(
                        f"Fetched repo page. total_requests_made={self._total_pages_fetched}, repo_issue_count={issues['totalCount']}, repo_pr_count={prs['totalCount']} issue_cursor={issue_cursor or '-'} pr_cursor={pr_cursor or '-'}"
                    )
            except (SystemExit, KeyboardInterrupt):
                logger.warning("Interrupted, will convert retrieved data and exit")
                was_interrupted = True
                break

        # Merge all the pages (including comments) into one big response object
        # by extending the list of nodes in the first page. This makes it easier
        # for the rest of the code to deal with it rather than passing around
        # one page at a time. The size of the response data is small enough that
        # memory shouldn't be a concern.
        merged_pages = success_responses[0] if success_responses else {}
        for page in success_responses[1:]:
            merged_pages["data"]["repository"]["issues"]["nodes"].extend(
                page["data"]["repository"]["issues"]["nodes"]
            )
            merged_pages["data"]["repository"]["pullRequests"]["nodes"].extend(
                page["data"]["repository"]["pullRequests"]["nodes"]
            )
        if not was_interrupted:
            self._fetch_and_merge_comments(merged_pages)
        return merged_pages

    def _fetch_and_merge_comments(self, merged_pages: Dict[str, Any]) -> None:
        """
        For any issues/PRs that are found to have an additional page of comments
        available, fetch the comments and merge them with the original data.
        """
        if not merged_pages.get("data"):
            return

        all_nodes = (
            merged_pages["data"]["repository"]["issues"]["nodes"]
            + merged_pages["data"]["repository"]["pullRequests"]["nodes"]
        )

        for original_node in all_nodes:
            if not original_node["comments"]["pageInfo"]["hasNextPage"]:
                continue

            has_page, comment_cursor = (
                True,
                original_node["comments"]["pageInfo"]["endCursor"],
            )
            while has_page:
                try:
                    variables = {
                        "id": original_node["id"],
                        "perPage": self.per_page,
                        "commentCursor": comment_cursor,
                    }
                    data, err = self._post(
                        json={"query": self._NODE_COMMENT_QUERY, "variables": variables}
                    )
                    if err:
                        break
                    else:
                        comments = data["data"]["node"]["comments"]
                        if comments["nodes"]:
                            comment_cursor = comments["pageInfo"]["endCursor"]
                            has_page = comments["pageInfo"]["hasNextPage"]
                        else:
                            comment_cursor, has_page = None, False

                        logger.info(
                            f"Fetched page for additional comments. total_requests_made={self._total_pages_fetched}, issue_comment_count={comments['totalCount']}, comment_cusor={comment_cursor}"
                        )

                        # Merge these comments to the original data
                        original_node["comments"]["nodes"].extend(comments["nodes"])

                except (SystemExit, KeyboardInterrupt):
                    logger.warning("Interrupted, will convert retrieved data and exit")
                    break

    def fetch_and_decode_repository(
        self,
        repo_name: str,
        include_issues: bool,
        include_prs: bool,
        include_closed_issues: bool,
        include_closed_prs: bool,
    ) -> GithubRepo:
        """
        Entry point for fetching a repo.
        """
        logger.info(f"Initiating fetch for repo: {repo_name}")
        owner, repo = repo_name.split("/")
        response = self._fetch_repo(
            owner=owner,
            repo=repo,
            include_issues=include_issues,
            include_prs=include_prs,
            include_closed_issues=include_closed_issues,
            include_closed_prs=include_closed_prs,
        )

        try:
            repo_data = response["data"]["repository"]
        except KeyError:
            logger.error("Repository data missing in response, can't proceed")
            raise

        issues = []
        prs = []
        for i in repo_data["issues"]["nodes"]:
            try:
                issues.append(
                    self._parse_issue_or_pull_request(i, is_pull_request=False)
                )
            except Exception:
                logger.warning(f"Error parsing issue, skipping: {i}", exc_info=True)

        for pr in repo_data["pullRequests"]["nodes"]:
            try:
                prs.append(self._parse_issue_or_pull_request(pr, is_pull_request=True))
            except Exception:
                logger.warning(
                    f"Error parsing pull request, skipping: {pr}", exc_info=True
                )

        return GithubRepo(
            full_name=repo_data["nameWithOwner"],
            url=repo_data["url"],
            # We have to sort in application code because these are separate
            # objects in the GraphQL API.
            issues=sorted(issues + prs, key=lambda x: x.number, reverse=True),
        )

    def _parse_issue_or_pull_request(
        self, issue_or_pr: Dict[str, Any], is_pull_request: bool
    ) -> GithubIssue:
        i = issue_or_pr
        comments = []
        for c in i["comments"]["nodes"]:
            try:
                comments.append(
                    GithubComment(
                        created_at=dateutil_parse(c["createdAt"]),
                        body=c["body"],
                        user_login=c["author"]["login"]
                        if c.get("author")
                        else "(unknown)",
                        user_url=c["author"]["url"] if c.get("author") else "(unknown)",
                        user_avatar_url=c["author"]["avatarUrl"]
                        if c.get("author")
                        else "(unknown)",
                        url=c["url"],
                    )
                )
            except Exception:
                logger.warning(f"Error parsing comment, skipping: {c}", exc_info=True)
        return GithubIssue(
            pull_request=is_pull_request,
            user_login=i["author"]["login"] if i.get("author") else "(unknown)",
            user_url=i["author"]["url"] if i.get("author") else "(unknown)",
            user_avatar_url=i["author"]["avatarUrl"]
            if i.get("author")
            else "(unknown)",
            state=i["state"].lower(),
            body=i["body"],
            number=i["number"],
            title=i["title"],
            created_at=dateutil_parse(i["createdAt"]),
            url=i["url"],
            label_names=[node["name"] for node in i["labels"]["nodes"]],
            comments=comments,
        )


def export_issues_to_markdown_file(
    repo: GithubRepo,
    output_path: str,
    use_multiple_files: bool,
    is_idempotent: bool,
) -> None:
    """
    Given a GithubRepo type contained already-fetched data, convert it to markdown.
    """
    formatted_issues = {}
    for issue in repo.issues:
        try:
            slug, formatted_issue = format_issue_to_markdown(issue)
        except Exception:
            logger.info(
                "Couldn't process issue due to exceptions, skipping", exc_info=True
            )
            continue
        else:
            formatted_issues[slug] = formatted_issue

    if len(formatted_issues.keys()) == 0:
        if use_multiple_files:
            logger.info(f"No issues processed, cleaning up directory: {output_path}")
            os.rmdir(output_path)
        else:
            logger.info("No issues processed, exiting without writing to file")
        return None

    if is_idempotent:
        datestring = ""
    else:
        datestring = " Generated on {}.".format(
            datetime.datetime.now().strftime("%Y.%m.%d at %H:%M:%S")
        )

    if use_multiple_files:
        # Write one file per issue
        metadata_footnote = templates_markdown.ISSUE_FILE_FOOTNOTE.format(
            repo_name=repo.full_name,
            repo_url=repo.url,
            datestring=datestring,
        )
        for issue_slug, formatted_issue in formatted_issues.items():
            issue_file_markdown = "\n".join([formatted_issue, metadata_footnote])
            issue_path = os.path.join(output_path, f"{issue_slug}.md")
            logger.info("Writing to file: {}".format(issue_path))
            with open(issue_path, "wb") as out:
                out.write(issue_file_markdown.encode("utf-8"))
    else:
        # Write everything in one file
        full_markdown_export = templates_markdown.BASE.format(
            repo_name=repo.full_name,
            repo_url=repo.url,
            issues="\n".join(formatted_issues.values()),
            datestring=datestring,
        )
        logger.info("Writing to file: {}".format(output_path))
        with open(output_path, "wb") as out:
            out.write(full_markdown_export.encode("utf-8"))
    return None


def format_issue_to_markdown(issue: GithubIssue) -> Tuple[str, str]:
    """
    Given a Github issue, return a formatted markdown block for the issue and
    its comments.
    """
    # Process the comments for this issue
    formatted_comments = ""
    if issue.comments:
        comments = []
        for comment in issue.comments:
            # logger.info("Processing comment: {}".format(comment.url))
            this_comment = templates_markdown.COMMENT.format(
                author=comment.user_login,
                author_url=comment.user_url,
                avatar_url=comment.user_avatar_url,
                date=comment.created_at.strftime("%Y-%m-%d %H:%M"),
                url=comment.url,
                body=comment.body,
            )
            comments.append(this_comment.rstrip())

        formatted_comments += "\n\n".join(comments)

    number = str(issue.number)
    if issue.pull_request:
        number += " PR"
        slugtype = "pr"
    else:
        number += " Issue"
        slugtype = "issue"

    labels = ""
    if issue.label_names:
        labels = ", ".join(["`{}`".format(lab) for lab in issue.label_names])
        labels = "**Labels**: {}\n\n".format(labels)

    formatted_issue = templates_markdown.ISSUE.format(
        title=issue.title,
        date=issue.created_at.strftime("%Y-%m-%d %H:%M"),
        number=number,
        url=issue.url,
        author=issue.user_login,
        author_url=issue.user_url,
        avatar_url=issue.user_avatar_url,
        state=issue.state,
        body=issue.body,
        comments=formatted_comments,
        labels=labels,
    )
    slug = ".".join(
        [
            issue.created_at.strftime("%Y-%m-%d"),
            str(issue.number),
            slugtype,
            issue.state,
        ]
    )
    return slug, formatted_issue.replace("\r", "")


def get_environment_token() -> str:
    try:
        token = os.environ[ENV_GITHUB_TOKEN]
        logger.info("Using token from environment")
        return token
    except KeyError:
        for path in GITHUB_ACCESS_TOKEN_PATHS:
            logger.info(f"Looking for token in file: {path}")
            if os.path.exists(path):
                logger.info(f"Using token from file: {path}")
                with open(path, "r") as f:
                    token = f.read().strip()
                    return token


def main():
    """Entry point"""
    args = parse_args(sys.argv[1:])

    if args.use_multiple_files:
        if os.path.exists(args.output_path):
            if len(os.listdir(args.output_path)):
                raise RuntimeError(
                    f"Output directory already exists and has files in it: {args.output_path}"
                )
        else:
            logger.info(f"Creating output directory: {args.output_path}")
            os.mkdir(args.output_path)

    gh = GithubAPI(token=get_environment_token())
    repo = gh.fetch_and_decode_repository(
        args.repo,
        include_closed_prs=args.include_closed_prs,
        include_closed_issues=args.include_closed_issues,
        include_prs=args.include_prs,
        include_issues=args.include_issues,
    )

    # Log issue counts
    logger.info(f"Retrieved issues for repo: {repo.full_name}")
    counts = {
        "PRs": defaultdict(int),
        "issues": defaultdict(int),
        "total": len(repo.issues),
    }
    for issue in repo.issues:
        if issue.pull_request:
            counts["PRs"][issue.state] += 1
            counts["PRs"]["total"] += 1
        else:
            counts["issues"][issue.state] += 1
            counts["issues"]["total"] += 1
    counts["PRs"] = dict(counts["PRs"])
    counts["issues"] = dict(counts["issues"])
    logger.info(f"Retrieved issue counts: \n{pprint.pformat(counts)}")

    # Convert and save markdown
    logger.info("Converting retrieved issues to markdown")
    export_issues_to_markdown_file(
        repo=repo,
        output_path=args.output_path,
        use_multiple_files=args.use_multiple_files,
        is_idempotent=args.is_idempotent,
    )
    logger.info("Done.")


if __name__ == "__main__":
    sys.exit(main())
