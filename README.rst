gh2md
=====

|PyPI|  |Travis|

Dump issues and pull requests for a Github repository into a single, readable
markdown file.

There are various other projects that handle Github issue exports
(Eg. `offline-issues <https://github.com/jlord/offline-issues>`_), but I couldn't
find one that writes all issues, comments and metadata to a single readable
file.


Example exports
---------------

An example exported file is included in the `examples directory <examples/sshrc.md>`_.

Default behaviour is to export all issues and open PRs. Closed PRs are ignored.


Github workflow: backup issues as a markdown file in your repo
--------------------------------------------------------------

`@0ut0fcontrol <https://github.com/0ut0fcontrol>`_ contributed a github workflow
that uses `gh2md` to run a nightly export to `issues.md`, and push it back to
your repo. You can find the thread and workflow code `here
<https://github.com/mattduck/gh2md/issues/11>`_.

This has been added to the `gh2md` repo itself, so you can see an up-to-date
export in `issues.md <./issues.md>`_.


Usage
-----

Run export for ``pope/ob-go``, prompting for login to ``mygithubuser``::

    gh2md pope/ob-go ob-go.md --login mygithubuser


Run export for ``sarabander/sicp``, passing in token::

    gh2md sarabander/sicp sicp.md --token myAPItoken


Run export for ``paulirish/git-open``, pulling token from environment, and excluding closed PRs::

    export GITHUB_ACCESS_TOKEN=myAPItoken
    gh2md paulirish/git-open git-open.md --no-closed-prs


Run export for ``shezadkhan137/required``, pulling token from file, and excluding closed issues:::

    echo myAPItoken > ~/.github-token --no-closed-issues
    gh2md shezadkhan137/required required.md


Full help::

    usage: gh2md [-h] [-l LOGIN_USER] [-t TOKEN] [-I] [--no-prs] [--no-closed-prs]
                [--no-issues] [--no-closed-issues]
                repo outpath

    Export Github repository issues and comments into a single
    markdown file. https://github.com/mattduck/gh2md.

    Example: gh2md mattduck/gh2md my_issues.md

    Credentials are resolved in the following order:

    - The --login flag always takes precedence and will prompt for this user.
    - The --token flag.
    - A `GITHUB_ACCESS_TOKEN` environment variable.
    - An API token stored in ~/.github-token.

    positional arguments:
    repo                  Github repo to export, in format "owner/repo_name".
    outpath               Path to write exported issues.

    optional arguments:
    -h, --help            show this help message and exit
    -l LOGIN_USER, --login LOGIN_USER
                            Prompt to login as this Github user. If provided, this
                            takes precedence over any token found in the
                            environment. If not provided and no token is found,
                            you will be prompted to login as the repository owner.
    -t TOKEN, --token TOKEN
                            Automatically login with this Github API token. If
                            --login is provided, this is ignored.
    -I, --idempotent      Remove non-deterministic values like timestamps. Two
                            runs of gh2md will always produce the same result, as
                            long as the Github data has not changed.
    --no-prs              Don't include pull requests in the export.
    --no-closed-prs       Don't include closed pull requests in the export.
    --no-issues           Don't include issues in the export.
    --no-closed-issues    Don't include closed issues in the export.


Install
-------

``pip install gh2md``. Alternatively, clone the repository and run ``make install``.


TODO
-----

- Improve performance. Currently fetching issues using PyGithub is slow - I
  assume it's possible to bulk-fetch most of the data.

- Add flag to toggle inclusion of images.

- Support 2FA login - currently if 2FA is enabled on your account you must setup
  an access token.

.. |PyPI| image:: https://img.shields.io/pypi/v/gh2md.svg
   :target: https://pypi.python.org/pypi/gh2md

.. |Travis| image:: https://travis-ci.org/mattduck/gh2md.svg?branch=master
   :target: https://travis-ci.org/mattduck/gh2md
