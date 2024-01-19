.PHONY: test build install clean examples lint upload assert_new_pypi_version assert_clean_git

clean:
	rm -rf build dist

build:
	python setup.py sdist bdist_wheel

install:
	python setup.py install

test:
	tox

format:
	black src tests

lint:
	black src tests --check
	flake8 src

examples:
	rm -rf examples
	mkdir examples
	gh2md mattduck/gh2md examples/gh2md.md
	gh2md mattduck/gh2md examples/gh2md-multiple-files-example --multiple-files
	gh2md Russell91/sshrc examples/sshrc.md

release: clean build assert_clean_git assert_new_pypi_version
	twine upload --repository gh2md dist/"$$(python setup.py --name)"*
	git tag "v$$(python setup.py --version)"
	echo "Release successful. You probably want to push the new git tag."

assert_new_pypi_version:
	python3 -c "$$PYSCRIPT_ASSERT_NEW_VERSION"

assert_clean_git:
	if [ "$$(git status --porcelain)" != "" ]; then echo "Dirty git index, exiting." && exit 1; fi


# PYSCRIPT_ASSERT_NEW_VERSION ------------------------------
# Confirm that there isn't an existing PyPI build for this version.
define PYSCRIPT_ASSERT_NEW_VERSION

import subprocess, sys, requests

NAME = subprocess.check_output(['python', 'setup.py', '--name']).decode().strip()
LOCAL_VERSION = subprocess.check_output(['python', 'setup.py', '--version']).decode().strip()

pypi_data_url = 'https://pypi.python.org/pypi/{name}/json'.format(name=NAME)
pypi_resp = requests.get(pypi_data_url)
pypi_resp.raise_for_status()  # If not registered this will raise
pypi_data = pypi_resp.json()
for pypi_version, upload_data in pypi_data['releases'].items():
    if upload_data and LOCAL_VERSION == pypi_version:
        print('Found existing PyPI release to match local version {}, exiting'.format(LOCAL_VERSION))
        sys.exit(1)

endef
export PYSCRIPT_ASSERT_NEW_VERSION
