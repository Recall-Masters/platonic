SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	mypy platonic tests/**/*.py
	flake8 platonic tests

.PHONY: unit
unit:
	pytest tests

.PHONY: package
package:
	poetry check
	pip check
	# Ignoring sphinx@2 security issue for now, see:
  # https://github.com/miyakogi/m2r/issues/51
	safety check --full-report -i 38330

.PHONY: test
test: lint package unit


.PHONY: format
format:
	python makefile.py
