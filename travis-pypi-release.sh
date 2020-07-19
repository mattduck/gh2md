#!/bin/bash
set -e
if [ "$(make assert_clean_git assert_new_pypi_version; echo $?)" == "0" ]; then
    make release
    git push --quiet https://mattduck:$GITHUB_TAG_TOKEN@github.com/mattduck/gh2md.git --tags >/dev/null 2>&1
fi
pip install gh2md --upgrade
