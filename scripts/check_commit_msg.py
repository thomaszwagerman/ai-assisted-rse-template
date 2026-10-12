# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

"""Pre-commit ``commit-msg`` hook: require a Conventional Commits subject line."""

import re
import sys
from pathlib import Path

PATTERN = re.compile(
    r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)"
    r"(\([\w./-]+\))?!?: .{1,72}$"
)
PASSTHROUGH = ("Merge ", "Revert ", "fixup! ", "squash! ")


def main() -> int:
    """Validate the first line of the commit message file given as argv[1]."""
    subject = Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()[0:1]
    first = subject[0] if subject else ""
    if first.startswith(PASSTHROUGH) or PATTERN.match(first):
        return 0
    print(
        "Commit subject must follow Conventional Commits, e.g. "
        "'feat(core): add median'.\n"
        "Types: feat fix docs style refactor perf test build ci chore revert",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
