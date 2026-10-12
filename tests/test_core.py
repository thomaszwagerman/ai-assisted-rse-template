# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

import pytest

from project_name import mean


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1.0, 2.0, 3.0], 2.0),
        ([4.2], 4.2),
        ([-1.0, 1.0], 0.0),
        ([0.1, 0.2, 0.3], 0.2),
    ],
)
def test_mean_values(values: list[float], expected: float) -> None:
    # rel=1e-12 allows for float rounding (a few ulp, ~1e-16 relative); abs=1e-12 is
    # needed for the case whose expected value is 0.0, which a relative tolerance alone
    # can never match. Both are far tighter than any real mistake would be.
    assert mean(values) == pytest.approx(expected, rel=1e-12, abs=1e-12)


def test_mean_empty_raises() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        mean([])
