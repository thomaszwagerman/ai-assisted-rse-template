# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

import pytest

from project_name import mean


def test_mean_of_integers_as_floats() -> None:
    assert mean([1.0, 2.0, 3.0]) == pytest.approx(2.0)


def test_mean_single_value() -> None:
    assert mean([4.2]) == pytest.approx(4.2)


def test_mean_empty_raises() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        mean([])
