<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# Changelog

All notable changes are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project structure.
- `make audit` (`uv audit`) to check locked dependencies for known vulnerabilities.
- `.github/CODEOWNERS` so the maintainer is requested to review every PR, including
  Dependabot's.
- `SECURITY.md` with a private vulnerability reporting policy.
- `/audit` prompt and `.github/instructions/review.instructions.md`; reviewer agent now
  requires evidence for each finding.
- `implementer` agent and a read-only `/fair-review` prompt (replaces `/review-for-fair`).
- `/release` prompt, and an optional-install guide for the community
  [rseng-agent-skills](https://github.com/fdiblen/rseng-agent-skills)
  (`docs/community-skills.md`).
- Python 3.14 support (classifier and CI matrix).
- Smoke test for `scripts/init_template.py`.
- README section describing the template as opinionated and AI-assisted, with links to
  rseng-agent-skills, the RSQKit AI guide and the GenAI RSE paper; the initialisation
  script removes it from new projects.
- README badges for Lint, CodeQL, Release, PyPI and supported Python versions (PyPI
  badges show "not found" until the first publish). The PyPI badges use the template's
  repository name rather than `project-name`, which belongs to an unrelated PyPI
  project; the initialisation script replaces it with your package name.
- README repostatus.org badge (WIP) and an alpha maturity note; the `/release` prompt and
  the template guide remind you to keep them consistent with the `Development Status`
  classifier.

### Changed

- Agents and prompts now point to `AGENTS.md` and the review instructions instead of
  restating them; `update-docs` is folded into the `docs-writer` agent.
- The template no longer ships its own skills; it points to the community pack instead.
- `make check` now also validates `pyproject.toml` and `CITATION.cff` (new `make metadata`
  target), and the Lint workflow calls the `make` targets, so local and CI checks match.
  Coverage XML is written only in CI; the community-skills page is merged into
  `docs/ai-workflow.md`; the README and getting-started no longer repeat the contributing
  commands.

### Removed

- `/new-feature` (superseded by the `implementer` agent) and `/prepare-release`
  (use `/release`) prompts.

[Unreleased]: https://github.com/thomaszwagerman/ai-assisted-rse-template/compare/HEAD...HEAD
