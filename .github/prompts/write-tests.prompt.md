---
description: Write or improve tests for the selected code or file
agent: agent
---

Write tests for ${input:target:File, function or selection to test}.

- Follow `.github/instructions/tests.instructions.md`. If the optional community skills
  are installed (see `AGENTS.md`), also use `rseng-testing`.
- Cover typical cases, edge cases (empty, single element, extreme values), and error paths.
- Use property-style or parametrised tests where they add value; keep them deterministic.
- Do not change production code unless you find a bug; report any bug you find instead of
  silently fixing it, with a failing test that demonstrates it.
- Run `uv run pytest` and report coverage for the target and the test results.
