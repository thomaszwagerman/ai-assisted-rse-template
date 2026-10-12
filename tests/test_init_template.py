# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

"""Smoke tests for the template initialisation script.

This file is template-only: ``scripts/init_template.py`` deletes it when it runs.
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "init_template.py"
VALID_ARGS = [
    "--name",
    "my-tool",
    "--author",
    "Ada Lovelace",
    "--email",
    "ada@example.org",
    "--org",
    "my-org",
    "--description",
    "Does something useful.",
]


def _run(*args: str, root: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "scripts" / "init_template.py"), *args],
        capture_output=True,
        text=True,
        check=False,
        cwd=root,
    )


def test_init_template_dry_run_changes_nothing() -> None:
    before = sorted(p.name for p in (ROOT / "src").iterdir())
    tracked = [ROOT / "README.md", ROOT / "pyproject.toml", ROOT / "CITATION.cff"]
    contents = {path: path.read_bytes() for path in tracked}

    result = _run(*VALID_ARGS, "--dry-run")

    assert result.returncode == 0, result.stderr
    assert "Dry run:" in result.stdout
    assert SCRIPT.exists()
    assert sorted(p.name for p in (ROOT / "src").iterdir()) == before
    assert {path: path.read_bytes() for path in tracked} == contents


def test_init_template_rejects_invalid_name() -> None:
    args = ["--name", "Bad_Name", *VALID_ARGS[2:], "--dry-run"]

    result = _run(*args)

    assert result.returncode == 2
    assert "--name must be lowercase" in result.stderr


def test_init_template_resets_changelog(tmp_path: Path) -> None:
    # Runs the real script on a copy so the working tree is never modified.
    copy = tmp_path / "repo"
    shutil.copytree(
        ROOT,
        copy,
        ignore=shutil.ignore_patterns(
            ".git",
            ".venv",
            "site",
            "dist",
            "__pycache__",
            ".mypy_cache",
            ".ruff_cache",
            ".pytest_cache",
            ".cache",
            "htmlcov",
        ),
    )

    result = _run(*VALID_ARGS, "--no-lock", root=copy)

    assert result.returncode == 0, result.stderr
    changelog = (copy / "CHANGELOG.md").read_text(encoding="utf-8")
    unreleased = changelog.split("## [Unreleased]")[1]
    assert "- Initial project structure." in unreleased
    assert "### Changed" not in unreleased
    assert "### Removed" not in unreleased
    assert "init_template" not in changelog
    assert "[Unreleased]: https://github.com/my-org/my-tool/compare/" in changelog
