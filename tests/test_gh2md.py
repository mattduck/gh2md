import os
import pytest
import mock
import six
import tempfile
import sys

from gh2md import gh2md


@pytest.fixture
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
