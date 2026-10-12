---
description: Testing conventions
applyTo: "tests/**/*.py"
---

- Use pytest; one behaviour per test, named `test_<unit>_<behaviour>`.
- Compare floats with `pytest.approx` and state the tolerance rationale when non-default.
- Use `pytest.mark.parametrize` for input tables; use `pytest.raises(..., match=...)`.
- Tests must be deterministic: fixed seeds, no network, no wall-clock dependence.
- Never loosen assertions or tolerances, or skip a test, just to get a green run.
- Fully typed (mypy strict applies to tests). Docstrings are not required.
