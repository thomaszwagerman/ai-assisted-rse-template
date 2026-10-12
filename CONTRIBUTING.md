<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# Contributing

Thank you for considering a contribution. This project follows the
[Sustainable Software Institute](https://www.software.ac.uk/) guidance and the
[FAIR4RS principles](https://doi.org/10.1038/s41597-022-01710-x).

## Getting set up

Requires [uv](https://docs.astral.sh/uv/) and `make`.

```bash
git clone https://github.com/thomaszwagerman/ai-assisted-rse-template
cd project-name
make install   # environment from uv.lock + pre-commit hooks
make check     # must pass before you open a pull request
```

Run `make help` to see every target.

## Workflow

1. Open or find an issue describing the change.
2. Branch from `main`: `git switch -c feat/short-description`.
3. Make small, focused commits using
   [Conventional Commits](https://www.conventionalcommits.org/) messages.
4. Add or update tests and documentation with the code.
5. Run `make check`. Pre-commit hooks run automatically on commit.
6. Open a pull request and fill in the template.

## Standards

- **Tests**: new behaviour needs tests; bug fixes need a regression test.
- **Typing and docs**: public functions are fully typed and have NumPy-style docstrings.
- **Licensing**: every file carries SPDX headers or is covered by `REUSE.toml`
  (`uv run reuse annotate --help`). `make reuse` checks this.
- **Dependencies**: add with `uv add` (or `uv add --group dev`) and commit `uv.lock`.
  Justify each new runtime dependency in the pull request.
- **Changelog**: user-visible changes go under "Unreleased" in
  [CHANGELOG.md](CHANGELOG.md).

## Using AI assistants

AI tools are welcome. You remain the author and are responsible for every line you
submit: read it, run it, and understand it before committing. Never paste secrets or
unpublished or sensitive data into an assistant. Agent configuration lives in
[AGENTS.md](AGENTS.md) and `.github/`.

## Releasing (maintainers)

Run the `/release` prompt (`.github/prompts/release.prompt.md`) in your AI assistant.

## Code of conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
