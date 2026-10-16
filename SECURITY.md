# Security policy

## Supported versions

Security fixes are applied to the latest released version and to `main`. Older versions
are not patched.

## Reporting a vulnerability

Please **do not open a public issue** for a security problem.

Report it privately, using either:

- GitHub's
  [private vulnerability reporting](https://github.com/thomaszwagerman/ai-assisted-rse-template/security/advisories/new)
  (Security tab, "Report a vulnerability"); or
- email **you@example.org**.

Include, as far as you can:

- the affected version or commit;
- a description of the problem and its impact;
- steps or a minimal example to reproduce it.

## What to expect

- We aim to acknowledge your report within 5 working days.
- We will keep you informed while we investigate, and tell you whether we accept the
  report as a vulnerability.
- Confirmed issues are fixed in a new release, noted in [CHANGELOG.md](CHANGELOG.md), and
  disclosed through a GitHub security advisory. We will credit you unless you prefer not
  to be named.

This is research software maintained on a best-effort basis; these timings are goals,
not guarantees.

## Scope

In scope: vulnerabilities in the code in this repository, its release workflow and its
published packages.

Out of scope: vulnerabilities in third-party dependencies (report those upstream; we
track them with Dependabot) and results that are scientifically wrong but not a security
problem (open a normal issue for those).
