---
description: Documentation conventions (Zensical)
applyTo: "docs/**/*.md,zensical.toml,README.md"
---

- Docs are built with Zensical from `zensical.toml` (`docs_dir = "docs"`); pages must be
  listed in `nav`. Verify with `make docs`.
- API reference comes from docstrings via `::: project_name` (mkdocstrings); fix the
  docstring, not the generated output.
- Every code example must be runnable as written; keep examples minimal.
- Markdown files start with the SPDX HTML comment header. Use relative links.
- Do not state benchmarks, results, or citations that you have not verified.
