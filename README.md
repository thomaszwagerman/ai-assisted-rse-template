<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# project-name

[![Tests](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/tests.yml/badge.svg)](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/tests.yml)
[![Lint](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/lint.yml/badge.svg)](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/lint.yml)
[![CodeQL](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/codeql.yml/badge.svg)](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/codeql.yml)
[![Docs](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/docs.yml/badge.svg)](https://thomaszwagerman.github.io/ai-assisted-rse-template/)
[![REUSE status](https://api.reuse.software/badge/github.com/thomaszwagerman/ai-assisted-rse-template)](https://api.reuse.software/info/github.com/thomaszwagerman/ai-assisted-rse-template)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/thomaszwagerman/ai-assisted-rse-template/badge)](https://scorecard.dev/viewer/?uri=github.com/thomaszwagerman/ai-assisted-rse-template)
[![Release](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/release.yml/badge.svg)](https://github.com/thomaszwagerman/ai-assisted-rse-template/actions/workflows/release.yml)
[![PyPI](https://img.shields.io/pypi/v/ai-assisted-rse-template.svg)](https://pypi.org/project/ai-assisted-rse-template/)
[![Python versions](https://img.shields.io/pypi/pyversions/ai-assisted-rse-template.svg)](https://pypi.org/project/ai-assisted-rse-template/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSES/MIT.txt)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

One-line description of the project.

<!-- template-about:start -->
> This is an *opinionated* repository template for research
> software engineers (RSEs) who want their work to be assisted by AI tools and agents.
> It attempts to pair RSE good practice with agent instructions, prompts and
> guard-rails.
>
> Recommended complimentary resources:
>
> - **Skills:** community agent skills for research software live in
>   [rseng-agent-skills](https://github.com/fdiblen/rseng-agent-skills).
> - **Guidance:** for AI guidance and good practice, see the
>   [RSQKit AI guide](https://everse.software/RSQKit/ai).
> - **RSE in the age of GenAI:** Druskat, S., Barker, M., Cosden, I., Geng, C., Haines, R., Katz, D. S.,
>   Shingleton, J. & van Werkhoven, B. (2026). *Research Software Engineers in the Age of
>   GenAI: Same Value, Changing Practice*. Zenodo.
>   [https://doi.org/10.5281/zenodo.20320179](https://doi.org/10.5281/zenodo.20320179)
>   ([blog post](https://www.researchsoft.org/blog/2026-05-28/)).
>
> **Status:** alpha. The template is usable, but its layout, prompts and agents may
> change between releases. See the [changelog](CHANGELOG.md).
<!-- template-about:end -->

> **Using this as a template?** Start with
> [docs/using-this-template.md](docs/using-this-template.md), then replace this README.

## Installation

```bash
pip install project-name
# or
uv add project-name
```

## Quick start

```python
from project_name import mean

mean([1.0, 2.0, 3.0])  # 2.0
```

## Development

Requires [uv](https://docs.astral.sh/uv/) and `make`. Run `make install` once, then
`make check` before every pull request; `make help` lists all targets. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow. For optional AI-assistant
skills, see [docs/ai-workflow.md](docs/ai-workflow.md#community-skills-optional).

## Citation

If you use this software, please cite it. GitHub's "Cite this repository" button
reads [CITATION.cff](CITATION.cff). Releases are archived on Zenodo; the DOI will
appear here once the first release is made.

## Licence

Code is released under the [MIT licence](LICENSES/MIT.txt). Licensing is
[REUSE](https://reuse.software)-compliant; see [REUSE.toml](REUSE.toml).
