# Changelog

## 1.0.0

- Add support for exporting one file per issue using `--multiple-files`.
- Add support for a token path in `~/.config/gh2md/token`.
- Upgrades to PyGithub 1.55.

Breaking changes:

- Remove support for username + password login, which was removed from the
  Github API back in 2020.

- Remove the `--token` argument. Tokens must now either be read from the
  environment or a file.
