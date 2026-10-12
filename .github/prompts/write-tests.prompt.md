---
description: Write or improve tests for the selected code or file
agent: agent
---

Write tests for ${input:target:File, function or selection to test}.

- Follow `.github/instructions/tests.instructions.md`. If the optional community skills
  are installed (see `docs/community-skills.md`), also use `rseng-testing`; where it
  disagrees with the instructions file or `AGENTS.md`, those win.
- Cover typical cases, edge cases (empty, single element, extreme values), and error paths.
- Use property-style or parametrised tests where they add value; keep them deterministic.
- Do not change production code unless you find a bug; report any bug you find instead of
  silently fixing it, with a failing test that demonstrates it.
- Run `uv run pytest` and report coverage for the target and the test results.
