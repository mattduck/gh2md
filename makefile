.PHONY: test build install clean examples

build:
		python setup.py sdist bdist_wheel

install:
		python setup.py install

test:
		tox

examples:
		rm -rf examples
		mkdir examples
		gh2md Russell91/sshrc examples/sshrc.md

clean:
		rm -rf build dist



