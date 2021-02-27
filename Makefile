SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy platonic tests
	poetry run flakehell lint platonic tests

.PHONY: unit
unit:
	# Pytest fails without this file
	touch platonic/__init__.py
	poetry run pytest
	rm -f platonic/__init__.py

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit

.PHONY: format
format:
	poetry run jeeves format
