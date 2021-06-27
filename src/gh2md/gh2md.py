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


def main():
    """Entry point"""
    args = parse_args(sys.argv[1:])
    gh = github_login()
    fetch_repo_and_export_to_markdown(
        gh=gh,
        repo_string=args.repo,
        output_path=args.output_path,
        use_multiple_files=args.use_multiple_files,
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


def fetch_repo_and_export_to_markdown(
    gh,
    repo_string,
    output_path,
    is_idempotent=False,
    use_multiple_files=False,
    include_issues=True,
    include_closed_issues=True,
    include_prs=True,
    include_closed_prs=True,
):
    """
    Main logic (excluding parsing args + login)
    """
    if use_multiple_files:
        if os.path.exists(output_path):
            if len(os.listdir(output_path)):
                raise RuntimeError(
                    f"Output directory already exists and has files in it: {output_path}"
                )
        else:
            logger.info(f"Creating output directory: {output_path}")
            os.mkdir(output_path)

    repo = get_github_repo(gh, repo_string)
    logger.info("Retrieved repo: {}".format(repo.full_name))
    export_issues_to_markdown_file(
        repo=repo,
        output_path=output_path,
        use_multiple_files=use_multiple_files,
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
    output_path,
    use_multiple_files,
    is_idempotent,
    include_closed_issues=True,
    include_closed_prs=True,
    include_issues=True,
    include_prs=True,
):
    """
    Export one repo
    """
    formatted_issues = {}
    try:
        if include_prs and include_closed_prs:
            filter_state = "all"
        elif include_issues and include_closed_issues:
            filter_state = "all"
        else:
            # we're only including open issues.
            filter_state = "open"
        # TODO: A way to just pass filters as args into this function?
        for issue in repo.get_issues(state=filter_state):
            # The Github API includes pull requests as "issues".
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
                logger.info(
                    "Caught exception checking issue or PR state, skipping",
                    exc_info=True,
                )
                continue

            # Try multiple times to process the issue and append to main issue list
            try:
                slug, formatted_issue = process_issue_to_markdown(issue)
            except Exception:
                logger.info(
                    "Couldn't process issue due to exceptions, skipping", exc_info=True
                )
                continue
            else:
                formatted_issues[slug] = formatted_issue
    except (KeyboardInterrupt, SystemExit):
        pass

    if len(formatted_issues.keys()) == 0:
        if use_multiple_files:
            logger.info(f"No issues found, cleaning up directory: {output_path}")
            os.rmdir(output_path)
        else:
            logger.info("No issues found, exiting without writing to file")
        return None

    logger.info("Found {} issues".format(len(formatted_issues.keys())))
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
            repo_url=repo.html_url,
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
            repo_url=repo.html_url,
            issues="\n".join(formatted_issues.values()),
            datestring=datestring,
        )
        logger.info("Writing to file: {}".format(output_path))
        with open(output_path, "wb") as out:
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
        slugtype = "pr"
    else:
        number += " Issue"
        slugtype = "issue"

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
    slug = ".".join(
        [
            issue.created_at.strftime("%Y-%m-%d"),
            str(issue.number),
            slugtype,
            issue.state,
        ]
    )
    return slug, formatted_issue.replace("\r", "")


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
        logger.info(f"Authenticated: {gh.get_user().login}")
    else:
        logger.warning("No token provided. Access to private repositories will fail")
    return gh


def get_environment_token():
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


if __name__ == "__main__":
    sys.exit(main())
