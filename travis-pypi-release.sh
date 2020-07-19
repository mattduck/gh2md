#!/bin/bash
set -e
if [ -z "$TWINE_USERNAME" ]; then exit 1; fi
if [ -z "$TWINE_PASSWORD" ]; then exit 1; fi
if [ -z "$GITHUB_TAG_TOKEN" ]; then exit 1; fi
git config --global user.email "builds@travis-ci.com"
git config --global user.name "Travis CI"
pip install -r dev-requirements.txt
git status
if [ "$(make assert_clean_git assert_new_pypi_version; echo $?)" == "0" ]; then
    make release
    git push --quiet https://mattduck:$GITHUB_TAG_TOKEN@github.com/mattduck/gh2md.git --tags >/dev/null 2>&1
fi
pip install gh2md --upgrade
