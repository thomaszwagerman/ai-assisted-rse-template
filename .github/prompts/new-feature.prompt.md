---
description: Plan and implement a feature test-first, following project conventions
agent: agent
---

Implement this feature: ${input:feature:Describe the feature or issue number}

1. Read the relevant code, tests and docs. Summarise your understanding and a short plan,
   and list any assumptions or open questions. Wait for confirmation if anything is
   ambiguous or requires a new dependency.
2. Write failing tests first (`tests/`), then the smallest implementation that passes them.
3. Add typed signatures and NumPy-style docstrings with units and assumptions.
4. Update docs and `CHANGELOG.md` (Unreleased).
5. Run `make check` and show the real result. Fix root causes; never weaken tests.
6. Finish with a summary: files changed, how it was verified, and remaining risks.
