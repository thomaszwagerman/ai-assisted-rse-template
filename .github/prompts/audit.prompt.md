---
description: Read-only audit of the code for correctness, reproducibility, units, tests and silent risks
agent: ask
tools: ['search', 'read']
---

Audit this repository's code. Read `.github/instructions/review.instructions.md` first and
follow it: its checks, its evidence rule, its report format and its "Not checked" line.

Scope: ${input:scope:folder or file to audit (leave empty for the whole repository)}

Map the scope first, then trace the main flows from inputs to outputs, going deepest
where a mistake would change results most. Say which parts you did not read.

This prompt changes nothing. It does not check FAIR metadata, citation files or licensing
of the repository; use `/fair-review` for that.
