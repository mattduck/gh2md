gh2md
=====

|PyPI|

Export issues and pull requests for a Github repository to a readable markdown
file. You can either create a single file for the repo, or a directory with one
file per issue. See usage instructions for how to filter by issue type and state.

There are various other projects that handle Github issue exports
(Eg. `offline-issues <https://github.com/jlord/offline-issues>`_), but I
couldn't find one that writes all issues, comments and metadata to a single
readable file.


Example exports
---------------

- Basic export in `examples directory <examples/sshrc.md>`_.
- `example directory with one issue per file <examples/gh2md-multiple-files-example>`_
- gh2md's `own issues in a single file <./issues.md>`_.

Default behaviour is to export all issues and PRs.


Usage
-----

Run export for ``paulirish/git-open``, pulling token from environment, and excluding closed PRs:::

    export GITHUB_ACCESS_TOKEN=myAPItoken
    gh2md paulirish/git-open git-open.md --no-closed-prs


Run export for ``shezadkhan137/required``, pulling token from file, and excluding closed issues:::

    echo myAPItoken > ~/.config/gh2md/token
    gh2md shezadkhan137/required required.md --no-closed-issues

Run export for public repository ``sarabander/sicp``, using no authentication and one file per issue:::

    gh2md sarabander/sicp sicp-issues --multiple-files --no-closed-prs

Run export for GitHub Enterprise Server or custom GitHub instance:::

    export GITHUB_API_URL=https://github.example.com/api/graphql
    export GITHUB_ACCESS_TOKEN=myAPItoken
    gh2md owner/repo-name output.md

Full help::

    usage: gh2md [-h] [--multiple-files] [-I] [--no-prs] [--no-closed-prs]
                [--no-issues] [--no-closed-issues]
                [--file-extension FILE_EXTENSION]
                repo output_path

    Export Github repository issues, pull requests and comments to markdown files:
    https://github.com/mattduck/gh2md

    Example: gh2md mattduck/gh2md my_issues.md

    Credentials are resolved in the following order:

    - A `GITHUB_ACCESS_TOKEN` environment variable.
    - An API token stored in ~/.config/gh2md/token or ~/.github-token.

    You can override the GitHub API endpoint by setting the `GITHUB_API_URL` environment
    variable. This defaults to "https://api.github.com/graphql" and requires no change when using github.com.

    To access private repositories, you'll need a token with the full "repo" oauth
    scope.

    By default, all issues and pull requests will be fetched. You can disable these
    using the --no... flags, eg. --no-closed-prs, or --no-prs.

    positional arguments:
    repo                  Github repo to export, in format "owner/repo_name".
    output_path           Path to write exported issues.

    optional arguments:
    -h, --help            show this help message and exit
    --multiple-files      Instead of one file, treat the given path as a
                            directory, and create one file per issue, using a
                            format '{created_at}.{issue_number}.{issue_type}.{issu
                            e_state}{file_extension}'.
    -I, --idempotent      Remove non-deterministic values like timestamps. Two
                            runs of gh2md will always produce the same result, as
                            long as the Github data has not changed.
    --no-prs              Don't include pull requests in the export.
    --no-closed-prs       Don't include closed pull requests in the export.
    --no-issues           Don't include issues in the export.
    --no-closed-issues    Don't include closed issues in the export.
    --file-extension FILE_EXTENSION
                            File extension for output files. Default is '.md'.


Install
-------

``pip install gh2md``. Alternatively, clone the repository and run ``make install``.


Authentication
---------------

``gh2md`` requires a Github access token to authenticate requests. To read your
private repositories, you'll need to provide a personal access token with the
full **repo** oauth scope.

**It's not possible to authenticate with a username and password**. Github used
to support this, but it was discontinued in 2020.


Private GitHub server support
---------------------------------

``gh2md`` supports GitHub Enterprise Server instances by allowing you to override
the API endpoint URL. Set the ``GITHUB_API_URL`` environment variable to point
to your GitHub Enterprise Server GraphQL API endpoint.

Usage with GitHub Enterprise Server:::

    export GITHUB_API_URL=https://github.example.com/api/graphql
    export GITHUB_ACCESS_TOKEN=myAPItoken
    gh2md owner/repo-name output.md

If no ``GITHUB_API_URL`` is specified, it defaults to ``https://api.github.com/graphql``.


Github workflow: backup issues as a markdown file in your repo
--------------------------------------------------------------

`@0ut0fcontrol <https://github.com/0ut0fcontrol>`_ contributed a github workflow
that uses ``gh2md`` to run a nightly export to ``issues.md``, and push it back to
your repo. You can find the thread and workflow code `here
<https://github.com/mattduck/gh2md/issues/11>`_.

This has been added to the ``gh2md`` repo itself, so you can see an up-to-date
export in `issues.md <./issues.md>`_.


.. |PyPI| image:: https://img.shields.io/pypi/v/gh2md.svg
   :target: https://pypi.python.org/pypi/gh2md
