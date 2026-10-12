---
description: Bring docs and docstrings in line with the code
agent: agent
---

Update the documentation to match the current code.

1. Compare public API in `src/project_name/` with docstrings, `docs/` and the README.
2. Fix missing or wrong docstrings (NumPy style, units, assumptions, examples).
3. Ensure examples run as written; verify them by running them.
4. Run `make docs` and fix warnings or broken links.
5. List what you changed and anything you could not verify.
