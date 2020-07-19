#!/bin/bash
set -e
if [ "$(make assert_clean_git assert_new_pypi_version; echo $?)" == "0" ]; then
    make release
fi
