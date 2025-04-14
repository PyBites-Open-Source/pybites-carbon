# default target
.PHONY: all
all: help setup lint typing test

help:
	#   Provided as a convience to run commands with uv
	#   setup  - installs the necessary development dependencies.
	#   lint   - lints the code
	#   typing - checks the type hints
	#   test   - tests the code

.PHONY: setup
setup:
	uv sync --dev

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: typing
typing:
	uv run mypy carbon tests

.PHONY: test
test:
	uv run pytest --cov --capture=tee-sys

.PHONY: ci
ci: lint test
