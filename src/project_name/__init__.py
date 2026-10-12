# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

"""One-line description of the project."""

from importlib.metadata import PackageNotFoundError, version

from project_name.core import mean

try:
    __version__ = version("project-name")
except PackageNotFoundError:  # pragma: no cover - running from an uninstalled tree
    __version__ = "unknown"

__all__ = ["__version__", "mean"]
