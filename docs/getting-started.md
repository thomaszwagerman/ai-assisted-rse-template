<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# Getting started

## Install

```bash
uv add project-name
# or: pip install project-name
```

## Use

```python
from project_name import mean

print(mean([1.0, 2.0, 3.0]))  # 2.0
```

## Develop

```bash
make install   # environment from uv.lock, plus git hooks
make check     # lint, type-check, test, licence compliance
make docs-serve
```
