---
name: release-checklist
description: Prepare a new release of this research software, including version bump, changelog, metadata consistency, and the exact tag/publish commands. Use when asked to release, bump the version, or prepare a tag.
---

# Release checklist

Never commit, tag, push or publish yourself. Prepare changes, then give the user the
commands.

1. Confirm the working tree is clean and on `main`, and `make check` passes.
2. Choose the version using [SemVer](https://semver.org/). Confirm it with the user.
3. Update the version in all places and keep them identical:
   - `pyproject.toml` (`uv version <new>` does this and refreshes `uv.lock`)
   - `CITATION.cff` (`version`, `date-released` as today's date)
   - `codemeta.json` (`version`)
4. In `CHANGELOG.md`, move "Unreleased" entries under `## [<new>] - YYYY-MM-DD`, start a
   new empty "Unreleased", and update the compare links.
5. Run `uv run cffconvert --validate`, `make reuse`, `make build` and `make docs`.
6. Check the wheel/sdist contents in `dist/` (licence files included, no stray files).
7. Give the user these commands to run themselves:

   ```bash
   git commit -am "chore(release): v<new>"
   git tag -s v<new> -m "v<new>"     # or -a if not signing
   git push origin main --tags
   ```

8. Remind the user of the one-off setup the workflow relies on: PyPI trusted publisher
   for `release.yml`, `pypi` environment, and the Zenodo-GitHub link. After the release,
   add the Zenodo DOI to `CITATION.cff`, `codemeta.json` and the README.
