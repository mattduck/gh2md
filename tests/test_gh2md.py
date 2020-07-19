import os
import pytest
import mock
import six
import tempfile
import time
import sys
from typing import List

from gh2md import gh2md


@pytest.fixture(scope="session")
def gh():
    token = gh2md.get_environment_token()
    gh = gh2md.github_login(token=token)
    return gh


def test_pygithub_login(gh):
    assert gh.get_user().name


def test_get_repo_returns_pygithub_repo():
    repo_name = "mattduck/dotfiles"
    token = gh2md.get_environment_token()
    repo, gh = gh2md.get_github_repo(repo_name, token=token)
    assert repo.html_url == "https://github.com/mattduck/dotfiles"


def test_processing_for_single_issue_produces_result():
    issue = mock.MagicMock()
    res = gh2md.process_issue_to_markdown(issue)
    assert res


def test_print_rate_limit_prints_limit(gh):
    with mock.patch("sys.stdout", new_callable=six.StringIO) as stdout:
        gh2md.print_rate_limit(gh)
        assert "rate limit" in stdout.getvalue().lower()


def test_script_from_entry_point_with_small_repo():
    fd, path = tempfile.mkstemp()
    test_args = ["gh2md", "mattduck/dotfiles", path]
    with mock.patch.object(sys, "argv", test_args):
        gh2md.main()

    assert os.path.exists(path)
    with open(path) as f:
        contents = f.read()
        assert "mattduck/dotfiles" in contents
        assert "issue" in contents.lower()
        assert "#1" in contents.lower()
    os.remove(path)


def _run_once(args: List[str]):
    fd, path = tempfile.mkstemp()
    try:
        with mock.patch.object(sys, "argv", args + [path]):
            gh2md.main()
        assert os.path.exists(path)
        with open(path) as f:
            output = f.read()
        return output
    except Exception:
        raise
    finally:
        os.remove(path)


def test_script_idempotent_flag_makes_two_runs_identical():
    # Flaky test: this is subject to the race condition that the issues actually
    # do change (or that time doesn't change). That happens very rarely on this
    # repo though, so although it's not good practice I'm OK with the risk.
    output1 = _run_once(["gh2md", "mattduck/dotfiles"])
    time.sleep(1)
    output2 = _run_once(["gh2md", "mattduck/dotfiles"])
    assert output1 != output2

    output3 = _run_once(["gh2md", "--idempotent", "mattduck/dotfiles"])
    time.sleep(1)
    output4 = _run_once(["gh2md", "-I", "mattduck/dotfiles"])
    assert output3 == output4


def test_pr_and_issue_flags_dont_error():
    _run_once(["gh2md", "mattduck/gh2md", "--no-closed-issues"])
    _run_once(["gh2md", "mattduck/gh2md", "--no-closed-prs"])
    _run_once(["gh2md", "mattduck/gh2md", "--no-issues"])
    _run_once(["gh2md", "mattduck/gh2md", "--no-prs"])
