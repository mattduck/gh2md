#!/usr/bin/env python
# coding: utf-8
import sys
import os
import argparse
import getpass
import datetime
import traceback

from github import Github
from retrying import retry

from . import templates_markdown

ENV_GITHUB_TOKEN = "GITHUB_ACCESS_TOKEN"
GITHUB_ACCESS_TOKEN_PATH = os.path.expanduser(os.path.join("~", ".github-token"))

DESCRIPTION = """Export Github repository issues, pull requests and comments
into a single markdown file. https://github.com/mattduck/gh2md.

Example: gh2md mattduck/gh2md my_issues.md

Credentials are resolved in the following order:

- The --login flag always takes precedence and will prompt for this user.
- The --token flag.
- A `{token}` environment variable.
- An API token stored in ~/.github-token.

By default, all issues and pull requests will be fetched. You can disable these
using the --no... flags, eg. --no-closed-prs, or --no-prs.

""".format(
    token=ENV_GITHUB_TOKEN
)


def main():
    """Entry point"""
    args = parse_args(sys.argv[1:])
    fetch_repo_and_export_to_markdown(
        repo_string=args.repo,
        output_path=args.outpath,
        gh_login_user=args.login_user,
        gh_token=args.token,
        is_idempotent=args.is_idempotent,
        include_prs=args.include_prs,
        include_issues=args.include_issues,
        include_closed_prs=args.include_closed_prs,
        include_closed_issues=args.include_closed_issues,
    )


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=DESCRIPTION, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "repo",
        help='Github repo to export, in format "owner/repo_name".',
        type=str,
        action="store",
        # TODO - validate this is in correct format.
    )
    parser.add_argument(
        "outpath", help="Path to write exported issues.", type=str, action="store",
    )
    parser.add_argument(
        "-l",
        "--login",
        help="Prompt to login as this Github user. If provided, this takes "
        "precedence over any token found in the environment. If not "
        "provided and no token is found, you will be prompted to login as "
        "the repository owner.",
        type=str,
        action="store",
        dest="login_user",
    )
    parser.add_argument(
        "-t",
        "--token",
        help="Automatically login with this Github API token. If --login is "
        "provided, this is ignored.",
        type=str,
        action="store",
        dest="token",
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
    repo_string,
    output_path,
    gh_login_user=None,
    gh_token=None,
    is_idempotent=False,
    include_issues=True,
    include_closed_issues=True,
    include_prs=True,
    include_closed_prs=True,
):
    if not gh_token:
        gh_token = get_environment_token()
    repo, github_api = get_github_repo(repo_string, gh_login_user, gh_token,)
    print("Retrieved repo: {}".format(repo.full_name))
    export_issues_to_markdown_file(
        repo=repo,
        outpath=output_path,
        is_idempotent=is_idempotent,
        include_closed_prs=include_closed_prs,
        include_closed_issues=include_closed_issues,
        include_prs=include_prs,
        include_issues=include_issues,
    )
    print_rate_limit(github_api)
    print("Done.")


def export_issues_to_markdown_file(
    repo,
    outpath,
    is_idempotent,
    include_closed_issues=True,
    include_closed_prs=True,
    include_issues=True,
    include_prs=True,
):
    formatted_issues = []
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
            traceback.print_exc()
            print("Caught exception checking issue or PR state, skipping")
            continue

        # Try multiple times to process the issue and append to main issue list
        try:
            formatted_issue = process_issue_to_markdown(issue)
        except Exception:
            traceback.print_exc()
            print("Couldn't process issue due to exceptions, skipping")
            continue
        else:
            formatted_issues.append(formatted_issue)

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
        print("No issues found, exiting without writing to file")
        return None
    print("Exported {} issues".format(len(formatted_issues)))
    print("Writing to file: {}".format(outpath))
    with open(outpath, "wb") as out:
        out.write(full_markdown_export.encode("utf-8"))
    return None


@retry(stop_max_attempt_number=3, stop_max_delay=15000, wait_fixed=5000)
def process_issue_to_markdown(issue):
    """Given a Github Issue, return a formatted Markdown block for the issue and
    its comments.

    """
    print("Processing issue: {}".format(issue.html_url))

    # Process the comments for this issue
    formatted_comments = ""
    if issue.comments:
        comments = []
        for comment in issue.get_comments():
            print("Processing comment: {}".format(comment.html_url))
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


def get_github_repo(repo_string, login_user=None, token=None):
    repo_owner, repo_name = repo_string.split("/")
    gh = github_login(login_user, token, fallback_user=repo_owner)
    gh_owner = gh.get_user(repo_owner)
    return gh_owner.get_repo(repo_name), gh


def github_login(login_user=None, token=None, fallback_user=None):
    assert login_user or token or fallback_user
    per_page = 100

    if login_user:
        password = getpass.getpass("Github password for {} :".format(login_user))
        return Github(login_or_token=login_user, password=password, per_page=per_page)

    if token:
        return Github(login_or_token=token, per_page=per_page)

    password = getpass.getpass("Github password for {} :".format(fallback_user))
    return Github(login_or_token=fallback_user, password=password, per_page=per_page)


def get_environment_token():
    return os.environ.get(ENV_GITHUB_TOKEN) or read_github_token_file()


def read_github_token_file(token_path=GITHUB_ACCESS_TOKEN_PATH):
    if not os.path.exists(token_path):
        return None
    with open(token_path, "r") as f:
        return f.read().strip()


def print_rate_limit(gh):
    limit = gh.get_rate_limit()
    print("Github API rate limit: {}".format(str(limit)))


if __name__ == "__main__":
    sys.exit(main())
