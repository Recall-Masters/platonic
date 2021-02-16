SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy platonic tests
	poetry run flakehell lint platonic tests

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit

.PHONY: format
format:
	poetry run python makefile.py
