---
description: Review the repository against FAIR4RS and SSI software-sustainability practice
agent: ask
tools: ['search', 'read']
---

Review this repository against the FAIR4RS principles (Findable, Accessible,
Interoperable, Reusable) and Software Sustainability Institute guidance.

Check and report, with file references:

- **Findable**: `CITATION.cff` and `codemeta.json` complete and consistent with
  `pyproject.toml` (name, version, authors, licence, URLs, keywords); DOI present once
  released; README says what the software does.
- **Accessible**: public repository, tagged releases, archived on Zenodo, docs published.
- **Interoperable**: standard formats, documented inputs/outputs, pinned and locked
  dependencies (`uv.lock`), supported Python versions stated and tested in CI.
- **Reusable**: clear licence, REUSE compliance, tests, docs, contribution guide,
  code of conduct, changelog, governance and maintainers named.
- **Sustainability**: CI, dependency updates, bus factor, PR template.

Output a table of findings (Pass / Gap / Unsure) with a prioritised list of fixes.
Do not invent facts; mark anything you cannot verify from the files as Unsure.
