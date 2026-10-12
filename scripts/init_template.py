# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

"""Fill in the placeholders of this template for a new project.

Run once, right after creating a repository from the template::

    uv run python scripts/init_template.py \\
        --name my-tool --author "Ada Lovelace" --email ada@example.org \\
        --org my-org --description "Does something useful."

Use ``--dry-run`` first to see what would change.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {
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
}
SKIP_FILES = {"uv.lock", "init_template.py", "coverage.xml", ".coverage"}
OLD_MODULE = "project_name"
GITHUB_URL = re.compile(r"github\.com/(?P<owner>[^/\"]+)/(?P<name>[^/\"]+)")

NAV_OLD = (
    '  { "Using this template" = [\n'
    '    "using-this-template.md",\n'
    '    "ai-workflow.md",\n'
    "  ] },\n"
)
NAV_NEW = '  { "AI-assisted workflow" = "ai-workflow.md" },\n'
README_BANNER = re.compile(r"> \*\*Using this as a template\?\*\*.*?\n\n", re.DOTALL)
README_ABOUT = re.compile(
    r"<!-- template-about:start -->\n.*?<!-- template-about:end -->\n\n", re.DOTALL
)
INDEX_BULLET = re.compile(
    r"- Setting up a new project from this template\?.*?\n(?=\n|\Z)", re.DOTALL
)
CHANGELOG_UNRELEASED = re.compile(
    r"(## \[Unreleased\]\n\n).*?(\n\[Unreleased\]:)", re.DOTALL
)
CHANGELOG_FRESH = r"\1### Added\n\n- Initial project structure.\n\2"


def text_files() -> list[Path]:
    """Return all non-binary project files that may contain placeholders."""
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if (
            not path.is_file()
            or SKIP_DIRS & set(rel.parts)
            or path.name in SKIP_FILES
            or path.suffix in {".pyc", ".png", ".jpg", ".ico"}
        ):
            continue
        files.append(path)
    return files


def template_repository() -> tuple[str, str]:
    """Return the (owner, name) of the template's own repository.

    Read from ``[project.urls] Repository`` so the script holds no hard-coded names.
    """
    with (ROOT / "pyproject.toml").open("rb") as fh:
        url = tomllib.load(fh)["project"]["urls"]["Repository"]
    match = GITHUB_URL.search(url)
    if match is None:
        raise SystemExit(f"Cannot parse a GitHub repository from {url!r}")
    return match["owner"], match["name"]


def build_replacements(args: argparse.Namespace) -> list[tuple[str, str]]:
    """Return ordered (old, new) replacements; specific ones come first."""
    parts = args.author.split()
    family = parts[-1] if len(parts) > 1 else args.author
    given = " ".join(parts[:-1]) if len(parts) > 1 else args.author
    module = args.name.replace("-", "_")
    owner, name = template_repository()
    return [
        ('family-names: "Name"', f'family-names: "{family}"'),
        ('given-names: "Your"', f'given-names: "{given}"'),
        ('"familyName": "Name"', f'"familyName": "{family}"'),
        ('"givenName": "Your"', f'"givenName": "{given}"'),
        ("One-line description of the project.", args.description),
        ("Your Name", args.author),
        ("you@example.org", args.email),
        (f"{owner}.github.io/{name}", f"{args.org}.github.io/{args.name}"),
        (f"{owner}/{name}", f"{args.org}/{args.name}"),
        # Bare template name, e.g. in the README's PyPI badges.
        (name, args.name),
        ("your-github-handle", args.handle or args.org),
        ("your-org", args.org),
        (OLD_MODULE, module),
        ("project-name", args.name),
    ]


def main() -> int:
    """Parse arguments and rewrite the repository in place."""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--name", required=True, help="distribution name, e.g. my-tool")
    p.add_argument("--author", required=True, help='full name, e.g. "Ada Lovelace"')
    p.add_argument("--email", required=True)
    p.add_argument("--org", required=True, help="GitHub user or organisation")
    p.add_argument("--handle", help="maintainer GitHub handle (default: --org)")
    p.add_argument("--description", required=True, help="one-line description")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-lock", action="store_true", help="skip uv lock and uv sync")
    args = p.parse_args()

    if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", args.name):
        p.error("--name must be lowercase letters, digits and single hyphens")
    old_dir = ROOT / "src" / OLD_MODULE
    if not old_dir.is_dir():
        p.error(f"{old_dir} not found: has this template already been initialised?")

    replacements = build_replacements(args)
    changed = 0
    for path in text_files():
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        text = original
        rel = path.relative_to(ROOT).as_posix()
        if rel == "zensical.toml":
            text = text.replace(NAV_OLD, NAV_NEW)
        elif rel == "README.md":
            text = README_ABOUT.sub("", README_BANNER.sub("", text))
        elif rel == "docs/index.md":
            text = INDEX_BULLET.sub("", text)
        elif rel == "CHANGELOG.md":
            text = CHANGELOG_UNRELEASED.sub(CHANGELOG_FRESH, text)
        for old, new in replacements:
            text = text.replace(old, new)
        if text != original:
            changed += 1
            print(f"update {rel}")
            if not args.dry_run:
                path.write_text(text, encoding="utf-8")

    new_dir = ROOT / "src" / args.name.replace("-", "_")
    print(f"rename src/{OLD_MODULE} -> src/{new_dir.name}")
    guide = ROOT / "docs" / "using-this-template.md"
    smoke_test = ROOT / "tests" / "test_init_template.py"
    print(
        "delete docs/using-this-template.md, tests/test_init_template.py "
        "and scripts/init_template.py"
    )
    if args.dry_run:
        print(f"\nDry run: {changed} file(s) would change.")
        return 0

    old_dir.rename(new_dir)
    guide.unlink(missing_ok=True)
    smoke_test.unlink(missing_ok=True)
    if not args.no_lock:
        if shutil.which("uv") is None:
            print("uv not found; install it, then run `uv lock && make install`.")
            return 1
        subprocess.run(["uv", "lock"], cwd=ROOT, check=True)
        subprocess.run(["uv", "sync", "--all-groups"], cwd=ROOT, check=True)
    print(
        f"\nDone: {changed} file(s) updated. Next: add your ORCID to CITATION.cff, "
        "run `make install && make check`, then commit."
    )
    # One-off script: remove it so it cannot be run twice.
    Path(__file__).unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
