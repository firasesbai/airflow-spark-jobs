MYPY_OPTIONS = --ignore-missing-imports --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs

.PHONY: tests
tests:
	PYTHONPATH=. poetry run pytest -vv tests

.PHONY: lint-check
lint-check:
	poetry run pylint data_transformations tests

.PHONY: type-check
type-check:
	poetry run mypy ${MYPY_OPTIONS} data_transformations tests

.PHONY: style-checks
style-checks: lint-check type-check
