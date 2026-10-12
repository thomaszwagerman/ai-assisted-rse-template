---
description: Python code conventions for the package
applyTo: "src/**/*.py,scripts/**/*.py"
---

- Full type annotations; code must pass `mypy --strict` (`make typecheck`).
- NumPy-style docstrings (Parameters, Returns, Raises, Examples) on every public object.
  Include units and assumptions for scientific quantities.
- Raise specific exceptions with clear messages; do not use bare `except` or `assert` for
  input validation.
- Use `pathlib`, `collections.abc` types and f-strings; no mutable default arguments.
- Randomness: accept a `numpy.random.Generator` or an explicit `seed`; never seed globally.
- Public API is what `project_name/__init__.py` exports (`__all__`); keep it small.
- Each file starts with SPDX headers (see existing files).
- Formatting and lint are owned by Ruff; do not hand-format or add `# noqa` without a reason.
