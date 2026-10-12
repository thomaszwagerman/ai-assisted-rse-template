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
- `/audit` prompt and `scientific-code-review` skill; reviewer agent now requires evidence
  for each finding.
- `implementer` agent and `fair-review` skill with a read-only `/fair-review` prompt
  (replaces `/review-for-fair`).
- Python 3.14 support (classifier and CI matrix).
- Smoke test for `scripts/init_template.py`.

### Changed

- Agents and prompts now point to `AGENTS.md` and the skills instead of restating them;
  `update-docs` is folded into the `docs-writer` agent.

### Removed

- `/new-feature` (superseded by the `implementer` agent) and `/prepare-release`
  (use the `release-checklist` skill) prompts.

[Unreleased]: https://github.com/your-org/project-name/compare/HEAD...HEAD
