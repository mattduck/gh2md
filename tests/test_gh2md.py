'''
Test suite.

Prerequisites:

$ pip3 install mock pytest
$ pip3 install -e .
$ export GITHUB_ACCESS_TOKEN=<token>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

Run tests:

$ pytest
'''

import datetime
import os
import sys
import tempfile
import time
from typing import List

import mock
import pytest

from gh2md import gh2md


@pytest.fixture(scope="session")
def gh():
    return gh2md.GithubAPI(gh2md.get_environment_token())


def test_fetch_and_decode_repository(gh):
    repo = gh.fetch_and_decode_repository(
        "mattduck/dotfiles",
        include_issues=True,
        include_prs=True,
        include_closed_issues=True,
        include_closed_prs=True,
    )
    assert repo.url == "https://github.com/mattduck/dotfiles"
    assert repo.full_name == "mattduck/dotfiles"
    assert repo.issues


def test_processing_for_single_issue_produces_result():
    issue = gh2md.GithubIssue(
        pull_request=False,
        created_at=datetime.datetime.now(),
        number=5,
        state="closed",
        user_login="mattduck",
        user_url="https://example.com",
        user_avatar_url="https://example.com/avatar",
        body="test body",
        comments=[],
        label_names=[],
        title="test title",
        url="https://example.com/issue",
    )
    slug, content = gh2md.format_issue_to_markdown(issue)
    assert content
    assert str(issue.number) in slug
    assert issue.state in content
    assert issue.title in content
    assert issue.url in content
    assert issue.body in content


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


def test_script_idempotent_flag_and_pagination_produce_identical_runs(monkeypatch):
    # Flaky test: this is subject to the race condition that the issues actually
    # do change (or that time doesn't change). That happens very rarely on this
    # repo though, so although it's not good practice I'm OK with the risk.
    output1 = _run_once(["gh2md", "mattduck/gh2md"])
    time.sleep(1)
    output2 = _run_once(["gh2md", "mattduck/gh2md"])
    assert output1 != output2

    output3 = _run_once(["gh2md", "--idempotent", "mattduck/gh2md"])
    time.sleep(1)
    output4 = _run_once(["gh2md", "-I", "mattduck/gh2md"])
    assert output3 == output4

    time.sleep(1)
    monkeypatch.setenv("_GH2MD_PER_PAGE_OVERRIDE", "2")
    output5 = _run_once(["gh2md", "-I", "mattduck/gh2md"])
    assert output5 == output4


def test_script_runs_with_multiple_files_flag():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_args = ["gh2md", "mattduck/gh2md", "--multiple-files", tmpdir]
        with mock.patch.object(sys, "argv", test_args):
            gh2md.main()
        assert os.path.exists(tmpdir)
        files = os.listdir(tmpdir)
        assert len(files) > 10, "Expected more than 10 issue files for repo"
        for fname in files:
            with open(os.path.join(tmpdir, fname)) as f:
                contents = f.read()
                assert "gh2md" in contents


def test_pr_and_issue_flags_dont_error():
    _run_once(["gh2md", "mattduck/gh2md", "--no-closed-issues"])
    _run_once(["gh2md", "mattduck/gh2md", "--no-closed-prs"])
    _run_once(["gh2md", "mattduck/gh2md", "--no-issues"])
    _run_once(["gh2md", "mattduck/gh2md", "--no-prs"])

def test_invalid_repo_produces_error():
    repo_name = "https://github.com/mattduck/gh2md"
    with tempfile.TemporaryDirectory() as tmpdir:
        test_args = ["gh2md", repo_name, tmpdir]
        with mock.patch.object(sys, "argv", test_args):
            with pytest.raises(Exception) as exc_info:
                gh2md.main()
            assert exc_info.value.args[0] == f"Repo name is not of the form owner/repo: {repo_name}"
