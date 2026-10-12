---
description: GitHub Actions workflow security rules
applyTo: ".github/workflows/**/*.yml"
---

- Pin every third-party action to a full commit SHA with the version in a trailing
  comment (`uses: owner/repo@<sha> # v1.2.3`). For annotated tags, use the peeled commit
  SHA. Dependabot keeps pins current.
- Set top-level `permissions: contents: read`; grant extra scopes per job only.
- Use `persist-credentials: false` on checkout unless the job pushes.
- Never interpolate untrusted input (`github.event.*`, PR titles, branch names) directly
  into `run:` scripts; pass it through `env:`.
- Use `uv sync --locked` so CI fails when `uv.lock` is stale.
- Do not add secrets; use OIDC trusted publishing for PyPI.
