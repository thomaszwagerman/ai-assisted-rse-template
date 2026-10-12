<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# project-name

[![Tests](https://github.com/your-org/project-name/actions/workflows/tests.yml/badge.svg)](https://github.com/your-org/project-name/actions/workflows/tests.yml)
[![Docs](https://github.com/your-org/project-name/actions/workflows/docs.yml/badge.svg)](https://your-org.github.io/project-name/)
[![REUSE status](https://api.reuse.software/badge/github.com/your-org/project-name)](https://api.reuse.software/info/github.com/your-org/project-name)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/your-org/project-name/badge)](https://scorecard.dev/viewer/?uri=github.com/your-org/project-name)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSES/MIT.txt)

One-line description of the project.

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

Requires [uv](https://docs.astral.sh/uv/) and `make`.

```bash
make install   # create the environment and install git hooks
make check     # lint, type-check, test, licence compliance
make docs      # build the documentation
make help      # list all targets
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## Citation

If you use this software, please cite it. GitHub's "Cite this repository" button
reads [CITATION.cff](CITATION.cff). Releases are archived on Zenodo; the DOI will
appear here once the first release is made.

## Licence

Code is released under the [MIT licence](LICENSES/MIT.txt). Licensing is
[REUSE](https://reuse.software)-compliant; see [REUSE.toml](REUSE.toml).
