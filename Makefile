# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

.DEFAULT_GOAL := help

.PHONY: help install test lint format typecheck reuse metadata docs docs-serve build check clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Create the environment (dev + docs) from uv.lock and install git hooks
	uv sync --locked --all-groups
	uv run pre-commit install

test: ## Run the test suite with coverage
	uv run pytest

lint: ## Check code style and static rules
	uv run ruff check .
	uv run ruff format --check .

format: ## Auto-fix lint issues and format the code
	uv run ruff check --fix .
	uv run ruff format .

typecheck: ## Run mypy in strict mode
	uv run mypy

reuse: ## Check REUSE / SPDX licence compliance
	uv run reuse lint

metadata: ## Validate pyproject.toml and CITATION.cff
	uv run validate-pyproject pyproject.toml
	uv run cffconvert --validate

docs: ## Build the documentation site into ./site
	uv run --group docs zensical build --clean

docs-serve: ## Serve the documentation locally with live reload
	uv run --group docs zensical serve

build: ## Build sdist and wheel into ./dist
	uv build

check: lint typecheck test reuse metadata ## Run every check that CI runs

clean: ## Remove build and cache artefacts
	rm -rf dist site .cache .coverage coverage.xml .pytest_cache .mypy_cache .ruff_cache
