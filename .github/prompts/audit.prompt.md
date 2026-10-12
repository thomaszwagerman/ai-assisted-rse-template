---
description: Read-only audit of the code for correctness, reproducibility, units, tests and silent risks
agent: ask
tools: ['search', 'read']
---

Audit this repository's code using the `scientific-code-review` skill
(`.github/skills/scientific-code-review/SKILL.md`). Read that file first and follow it.

Scope: ${input:scope:folder or file to audit (leave empty for the whole repository)}

1. Map first: read the README, `pyproject.toml`, the entry points, the tests and the docs
   for the scope. State how you assume the code is used.
2. Trace the main flows from inputs to outputs. Go deep where a mistake would change
   results most. Say which parts you did not read.
3. Report in the format defined by the skill, at most 20 findings.

This prompt changes nothing. It does not check FAIR metadata, citation files or licensing
of the repository; use `/review-for-fair` for that.
