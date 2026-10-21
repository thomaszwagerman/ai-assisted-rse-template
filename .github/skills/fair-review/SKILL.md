---
name: fair-review
description: Read-only review of FAIR4RS and software-sustainability metadata and practice
disable-model-invocation: true
---
Review this repository's metadata and sustainability against FAIR4RS and Software
Sustainability Institute practice. This prompt changes nothing: report findings, never
edit files. Follow `AGENTS.md`. Do not invent facts; mark anything you cannot verify from
the files as **Unsure**.

If the optional community skills are installed (see `AGENTS.md`), also use
`rseng-fair-software` and `rseng-citation-metadata` for the detail. If not, carry on
without them.

Check and report, with file references:

- **Findable:** `CITATION.cff` and `codemeta.json` complete and consistent with
  `pyproject.toml` (name, version, authors, licence, URLs, keywords); DOI present once
  released; README says what the software does.
- **Accessible:** public repository, tagged releases, archived on Zenodo, docs published.
- **Interoperable:** standard formats, documented inputs and outputs, pinned and locked
  dependencies (`uv.lock`), supported Python versions stated and tested in CI.
- **Reusable:** clear licence, REUSE compliance (`make reuse`; report Unsure if you
  cannot run commands), tests, docs, contribution guide, code of conduct, changelog,
  governance and maintainers named.
- **Sustainability:** CI, dependency updates, bus factor, PR template.

Some items (Zenodo archive, public visibility, published docs, branch protection) cannot
be seen from the files; list them as Unsure rather than Pass.

## Output

A table of findings (Pass / Gap / Unsure) with a file reference per row, then a
prioritised list of fixes. End with `Not checked:` for what you could not read or run.

This prompt does not review code correctness; use `/audit` for that.
