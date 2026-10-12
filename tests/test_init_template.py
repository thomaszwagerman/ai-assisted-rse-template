# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

"""Smoke tests for the template initialisation script.

This file is template-only: ``scripts/init_template.py`` deletes it when it runs.
"""

import shutil
import subprocess
import sys
import tomllib
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


def _initialised_copy(tmp_path: Path) -> Path:
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
    return copy


def test_init_template_resets_changelog(tmp_path: Path) -> None:
    copy = _initialised_copy(tmp_path)
    changelog = (copy / "CHANGELOG.md").read_text(encoding="utf-8")
    unreleased = changelog.split("## [Unreleased]")[1]
    assert "- Initial project structure." in unreleased
    assert "### Changed" not in unreleased
    assert "### Removed" not in unreleased
    assert "init_template" not in changelog
    assert "[Unreleased]: https://github.com/my-org/my-tool/compare/" in changelog


def test_init_template_removes_template_banners_from_readme(tmp_path: Path) -> None:
    template_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "template-about:start" in template_readme
    copy = _initialised_copy(tmp_path)

    readme = (copy / "README.md").read_text(encoding="utf-8")

    assert "opinionated" not in readme
    assert "template-about" not in readme
    assert "Using this as a template" not in readme
    assert "## Installation" in readme
    assert "Does something useful." in readme


def test_init_template_points_pypi_badges_at_the_new_project(tmp_path: Path) -> None:
    # "project-name" is someone else's PyPI project, so the template's badges must
    # use another name; the script swaps it for the new project's name.
    template_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "img.shields.io/pypi/v/project-name" not in template_readme
    assert "pypi.org/project/project-name" not in template_readme

    readme = (_initialised_copy(tmp_path) / "README.md").read_text(encoding="utf-8")

    assert "https://img.shields.io/pypi/v/my-tool.svg" in readme
    assert "https://img.shields.io/pypi/pyversions/my-tool.svg" in readme
    assert "https://pypi.org/project/my-tool/" in readme
    assert "ai-assisted-rse-template" not in readme


def test_init_template_rewrites_template_repository_urls(tmp_path: Path) -> None:
    with (ROOT / "pyproject.toml").open("rb") as fh:
        template_url = tomllib.load(fh)["project"]["urls"]["Repository"]
    owner, name = template_url.removeprefix("https://github.com/").split("/")
    copy = _initialised_copy(tmp_path)

    for path in copy.rglob("*"):
        if path.is_file() and path.name != "uv.lock":
            text = path.read_text(encoding="utf-8", errors="ignore")
            assert f"{owner}/{name}" not in text, path
            assert f"{owner}.github.io" not in text, path
    pyproject = (copy / "pyproject.toml").read_text(encoding="utf-8")
    assert 'Repository = "https://github.com/my-org/my-tool"' in pyproject
    assert 'Documentation = "https://my-org.github.io/my-tool/"' in pyproject
