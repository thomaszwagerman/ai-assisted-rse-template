<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# Using this template

This page is deleted automatically when you run the initialisation script.

## 1. Create your repository

1. On GitHub click **Use this template**, then **Create a new repository**. Make it
   **public** if you plan to use OpenSSF Scorecard, Zenodo and GitHub Pages for free.
2. Clone it and open it in VS Code. Accept the recommended extensions.
3. Install [uv](https://docs.astral.sh/uv/) and `make` if you do not have them.

## 2. Fill in the placeholders

```bash
uv run python scripts/init_template.py --dry-run \
    --name my-tool --author "Ada Lovelace" --email ada@example.org \
    --org my-org --description "Does something useful."
```

Review the output, then run it again without `--dry-run`. The script replaces
`project-name`, `project_name`, `Your Name`, `you@example.org`, `your-org` and the
description everywhere, renames `src/project_name/`, resets the "Unreleased" section of
`CHANGELOG.md`, refreshes `uv.lock`, and removes this page, the script's own smoke test
(`tests/test_init_template.py`) and itself.

Then, by hand:

- Add your ORCID (and affiliation / ROR) in `CITATION.cff` and `codemeta.json`.
- Set `date-released` in `CITATION.cff` when you release.
- Replace the example `mean()` function, its tests and its docs with your own code.
- Check the licence choice (MIT by default). To change it: replace `LICENSES/MIT.txt` and
  `LICENSE` (`uv run reuse download <SPDX-ID>`), update `license` in `pyproject.toml`,
  `CITATION.cff`, `codemeta.json`, `REUSE.toml` and the SPDX headers.
- Update `GOVERNANCE.md` and the contact address in `CODE_OF_CONDUCT.md`.
- Edit `AGENTS.md` so the layout and conventions describe your real project.
- Add checks for your field (units, data formats, numerical methods) to the "Project-specific
  checks" section of `.github/skills/scientific-code-review/SKILL.md`.

Then verify everything:

```bash
make install
make check
make docs
```

## 3. Configure GitHub (once per repository)

| Setting | Where | Why |
|---|---|---|
| Pages source = **GitHub Actions** | Settings, Pages | `docs.yml` deploys the site |
| Branch protection on `main` | Settings, Rules | Require pull request and the `Tests`, `Lint`, `REUSE compliance` and `CodeQL` checks |
| Dependabot alerts and security updates | Settings, Advanced Security | Alerts for vulnerable dependencies |
| Secret scanning and push protection | Settings, Advanced Security | Stops leaked credentials |
| Environment `pypi` | Settings, Environments | Add yourself as a required reviewer for releases |
| PyPI trusted publisher | pypi.org, project, Publishing | Workflow `release.yml`, environment `pypi`; no token needed |
| Zenodo link | zenodo.org, GitHub settings | Enable the repository **before** the first release so the DOI is minted |

## 4. Releasing

Follow `.github/skills/release-checklist/SKILL.md`, or ask Copilot Chat to follow the
`release-checklist` skill. Publishing a GitHub release triggers Zenodo,
which reads `CITATION.cff`. Add the DOI back into `CITATION.cff`, `codemeta.json` and the
README afterwards.

## 5. Caveats

- Zensical is pre-1.0. Its version is locked in `uv.lock`; read the release notes before
  upgrading, and run `make docs` after every upgrade.
- OpenSSF Scorecard publishes only for public repositories. A modest score on a small
  project is normal; use it as a to-do list.
- CodeQL is free for public repositories only.
