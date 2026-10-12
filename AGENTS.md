<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# AGENTS.md

Instructions for AI coding agents (GitHub Copilot, Claude Code, Codex, Cursor, ...).
Humans: see [CONTRIBUTING.md](CONTRIBUTING.md). Keep this file short and accurate; if a
command here stops working, fix this file in the same change.

## Project

`project-name` is research software (Python >= 3.11, `src/` layout, package
`project_name`). Priorities, in order: **correctness and reproducibility**, clarity,
maintainability, then performance.

## Commands

Use `make` targets (they wrap `uv run`). Never call `pip` directly.

| Task | Command |
|---|---|
| Install environment and git hooks | `make install` |
| Everything CI runs | `make check` |
| Tests with coverage | `make test` (single test: `uv run pytest tests/test_core.py -k name`) |
| Lint / format | `make lint` / `make format` |
| Type check (mypy strict) | `make typecheck` |
| Licence compliance (REUSE) | `make reuse` |
| Build / preview docs (Zensical) | `make docs` / `make docs-serve` |
| Add a dependency | `uv add <pkg>` (runtime) or `uv add --group dev <pkg>` |

Run `make check` before declaring a task done, and report the actual output.

## Layout

- `src/project_name/`: library code. `tests/`: pytest tests mirroring the package.
- `docs/` + `zensical.toml`: documentation. API reference is generated from docstrings.
- `.github/`: workflows, issue/PR templates, Copilot instructions, prompts, agents, skills.
- `CITATION.cff`, `codemeta.json`, `REUSE.toml`: metadata. Keep them consistent.

## Conventions

- Type-annotate all code; mypy strict must pass. NumPy-style docstrings on public API.
- Prefer small pure functions. No hidden global state.
- Add or update tests with every behaviour change; bug fix = regression test first.
- Conventional Commits for messages (`feat(core): ...`); enforced by a hook.
- Every new file needs an SPDX header (`SPDX-FileCopyrightText`, `SPDX-License-Identifier`)
  or must be covered by `REUSE.toml`.
- Update `CHANGELOG.md` ("Unreleased") for user-visible changes.

## Scientific integrity rules

- Never invent data, results, references, DOIs, or citations. If unsure, say so.
- Make randomness reproducible: explicit seeds / `numpy.random.Generator`, no global seeding.
- State units, assumptions and sources in docstrings; do not silently change numerical
  behaviour. Flag any change that could alter published results.
- Do not weaken or delete tests, tolerances, or type checks to make a run pass.
- Never commit secrets, credentials, or non-public / personal data.

## Ask first

Stop and ask the user before you:

- add a runtime dependency, or change the supported Python versions;
- change the licence, `CITATION.cff` authorship, or `GOVERNANCE.md`;
- edit `uv.lock` by hand (use `uv lock` / `uv add`) or change `.github/workflows/`
  permissions or action pins;
- run destructive git operations, push, tag, or publish a release.

## Workflow

1. Read the relevant code and tests first. For non-trivial work, propose a short plan.
2. Make the smallest change that solves the problem; do not refactor unrelated code.
3. Run `make check`; fix failures at the root cause.
4. Summarise what changed, what you verified, and anything uncertain.
