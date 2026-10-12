# SPDX-FileCopyrightText: 2026 Your Name
#
# SPDX-License-Identifier: MIT

"""Core functionality. Replace this example with your own code."""

from collections.abc import Sequence


def mean(values: Sequence[float]) -> float:
    """Compute the arithmetic mean of a sequence of numbers.

    Parameters
    ----------
    values
        The numbers to average. Must not be empty.

    Returns
    -------
    float
        The arithmetic mean of ``values``.

    Raises
    ------
    ValueError
        If ``values`` is empty.

    Examples
    --------
    >>> mean([1.0, 2.0, 3.0])
    2.0
    """
    if len(values) == 0:
        msg = "mean() requires at least one value"
        raise ValueError(msg)
    return sum(values) / len(values)
