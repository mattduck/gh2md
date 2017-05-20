gh2md
=====

Dump issues for a Github repository into a single markdown file. 

There are various other projects that handle Github issue exports
(Eg. `offline-issues <https://github.com/jlord/offline-issues>`_), but I couldn't
find one that writes all issues, comments and metadata to a single readable
file.


Example exports
---------------

An example exported file is included in the `examples directory <examples/sshrc.md>`_. 

Default behaviour is to export all issues and open PRs. Closed PRs are ignored.


Usage
-----

Run export for ``pope/ob-go``, prompting for login to ``mygithubuser``::

    gh2md pope/ob-go ob-go.md --login mygithubuser


Run export for ``sarabander/sicp``, passing in token::

    gh2md sarabander/sicp sicp.md --token myAPItoken


Run export for ``paulirish/git-open``, pulling token from environment::

    export GITHUB_ACCESS_TOKEN=myAPItoken
    gh2md paulirish/git-open git-open.md


Run export for ``shezadkhan137/required``, pulling token from file::

    echo myAPItoken > ~/.github-token
    gh2md shezadkhan137/required required.md


Full help::

    $ gh2md -h
    usage: gh2md [-h] [-l LOGIN_USER] [-t TOKEN] repo outpath

    Export Github repository issues and comments into a single
    markdown file. https://github.com/mattduck/gh2md.

    Credentials are resolved in the following order:

    - The --login flag always takes precedence and will prompt for this user.
    - The --token flag.
    - A `GITHUB_ACCESS_TOKEN` environment variable.
    - An API token stored in `~/.github-token`.

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


Install
-------

``pip install gh2md``. Alternatively, clone the repository and run ``make install``.


TODO
-----

- Improve performance. Currently fetching issues using PyGithub is slow - I
  assume it's possible to bulk-fetch most of the data.

- Add flag to toggle inclusion of images.

- Add arg(s) to control which data is exported - open/closed, issues/PRs.

- Support 2FA login - currently if 2FA is enabled on your account you must setup
  an access token.
