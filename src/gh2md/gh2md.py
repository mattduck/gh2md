#!/usr/bin/env python
# coding: utf-8
import argparse
import datetime
import logging
import os
import sys

from github import Github
from retrying import retry

from . import templates_markdown

ENV_GITHUB_TOKEN = "GITHUB_ACCESS_TOKEN"
GITHUB_ACCESS_TOKEN_PATHS = [
    os.path.expanduser(os.path.join("~", ".config", "gh2md", "token")),
    os.path.expanduser(os.path.join("~", ".github-token")),
]

DESCRIPTION = """Export Github repository issues, pull requests and comments
into a single markdown file. https://github.com/mattduck/gh2md.

Example: gh2md mattduck/gh2md my_issues.md

Credentials are resolved in the following order:

- A `{token}` environment variable.
- An API token stored in ~/.config/gh2md/token or ~/.github-token.

To access your private repositories, you'll need a token with

By default, all issues and pull requests will be fetched. You can disable these
using the --no... flags, eg. --no-closed-prs, or --no-prs.

""".format(
    token=ENV_GITHUB_TOKEN
)

logformat = "[%(asctime)s] [%(levelname)s] %(msg)s"
logging.basicConfig(level=logging.INFO, format=logformat)
logger = logging.getLogger(__name__)


def main():
    """Entry point"""
    args = parse_args(sys.argv[1:])
    gh = github_login()
    fetch_repo_and_export_to_markdown(
        gh=gh,
        repo_string=args.repo,
        output_path=args.outpath,
        is_idempotent=args.is_idempotent,
        include_prs=args.include_prs,
        include_issues=args.include_issues,
        include_closed_prs=args.include_closed_prs,
        include_closed_issues=args.include_closed_issues,
    )


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
        "outpath",
        help="Path to write exported issues.",
        type=str,
        action="store",
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


def fetch_repo_and_export_to_markdown(
    gh,
    repo_string,
    output_path,
    is_idempotent=False,
    include_issues=True,
    include_closed_issues=True,
    include_prs=True,
    include_closed_prs=True,
):
    """
    Main logic (excluding parsing args + login)
    """
    repo = get_github_repo(gh, repo_string)
    logger.info("Retrieved repo: {}".format(repo.full_name))
    export_issues_to_markdown_file(
        repo=repo,
        outpath=output_path,
        is_idempotent=is_idempotent,
        include_closed_prs=include_closed_prs,
        include_closed_issues=include_closed_issues,
        include_prs=include_prs,
        include_issues=include_issues,
    )
    limit = gh.get_rate_limit()
    logger.info("Github API rate limit: {}".format(str(limit)))
    logger.info("Done.")


def export_issues_to_markdown_file(
    repo,
    outpath,
    is_idempotent,
    include_closed_issues=True,
    include_closed_prs=True,
    include_issues=True,
    include_prs=True,
):
    """
    Export one repo
    """
    formatted_issues = []
    try:
        for issue in repo.get_issues(state="all"):
            # The Github API includes pull requests as "issues". Skip
            # closed PRs, as they will add a lot of noise to the export.
            try:
                if issue.pull_request and not include_prs:
                    continue
                if (
                    issue.pull_request
                    and issue.state.lower() == "closed"
                    and (not include_closed_prs)
                ):
                    continue
                if (not issue.pull_request) and not include_issues:
                    continue
                if (
                    (not issue.pull_request)
                    and issue.state.lower() == "closed"
                    and (not include_closed_issues)
                ):
                    continue
            except Exception:
                logger.info("Caught exception checking issue or PR state, skipping", exc_info=True)
                continue

            # Try multiple times to process the issue and append to main issue list
            try:
                formatted_issue = process_issue_to_markdown(issue)
            except Exception:
                logger.info("Couldn't process issue due to exceptions, skipping", exc_info=True)
                continue
            else:
                formatted_issues.append(formatted_issue)
    except (KeyboardInterrupt, SystemExit):
        pass

    if is_idempotent:
        datestring = ""
    else:
        datestring = " Generated on {}.".format(
            datetime.datetime.now().strftime("%Y.%m.%d at %H:%M:%S")
        )
    full_markdown_export = templates_markdown.BASE.format(
        repo_name=repo.full_name,
        repo_url=repo.html_url,
        issues="\n".join(formatted_issues),
        datestring=datestring,
    )

    if len(formatted_issues) == 0:
        logger.info("No issues found, exiting without writing to file")
        return None
    logger.info("Exported {} issues".format(len(formatted_issues)))
    logger.info("Writing to file: {}".format(outpath))
    with open(outpath, "wb") as out:
        out.write(full_markdown_export.encode("utf-8"))
    return None


@retry(stop_max_attempt_number=3, stop_max_delay=15000, wait_fixed=5000)
def process_issue_to_markdown(issue):
    """
    Given a Github issue, return a formatted markdown block for the issue and
    its comments.
    """
    logger.info("Processing issue: {}".format(issue.html_url))

    # Process the comments for this issue
    formatted_comments = ""
    if issue.comments:
        comments = []
        for comment in issue.get_comments():
            logger.info("Processing comment: {}".format(comment.html_url))
            this_comment = templates_markdown.COMMENT.format(
                author=comment.user.name or comment.user.login,
                author_url=comment.user.html_url,
                avatar_url=comment.user.avatar_url,
                date=comment.created_at.strftime("%Y-%m-%d %H:%M"),
                url=comment.html_url,
                body=comment.body,
            )
            comments.append(this_comment.rstrip())

        formatted_comments += "\n\n".join(comments)

    number = str(issue.number)
    if issue.pull_request:
        number += " PR"
    else:
        number += " Issue"

    labels = ""
    if issue.labels:
        labels = ", ".join(["`{}`".format(lab.name) for lab in issue.labels])
        labels = "**Labels**: {}\n\n".format(labels)

    formatted_issue = templates_markdown.ISSUE.format(
        title=issue.title,
        date=issue.created_at.strftime("%Y-%m-%d %H:%M"),
        number=number,
        url=issue.html_url,
        author=issue.user.name or issue.user.login,
        author_url=issue.user.html_url,
        avatar_url=issue.user.avatar_url,
        state=issue.state,
        body=issue.body,
        comments=formatted_comments,
        labels=labels,
    )
    return formatted_issue.replace("\r", "")


def get_github_repo(gh, repo_string):
    """
    Retrieve a single repo
    """
    repo_owner, repo_name = repo_string.split("/")
    gh_owner = gh.get_user(repo_owner)
    return gh_owner.get_repo(repo_name)


def github_login():
    """
    Handle login
    """
    gh_token = get_environment_token()
    gh = Github(login_or_token=gh_token, per_page=100)
    if gh_token:
        logger.warning(f"Authenticated: {gh.get_user().login}")
    else:
        logger.info("No token provided. Access to private stuff will fail")
    return gh


def get_environment_token():
    try:
        return os.environ[ENV_GITHUB_TOKEN]
    except KeyError:
        for path in GITHUB_ACCESS_TOKEN_PATHS:
            logger.info(path)
            if os.path.exists(path):
                with open(path, "r") as f:
                    return f.read().strip()


if __name__ == "__main__":
    sys.exit(main())
