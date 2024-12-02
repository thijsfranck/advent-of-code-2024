from collections.abc import Generator, Iterable
from itertools import pairwise

MIN_INCLINE = 1
MAX_INCLINE = 3


def parse_input(data: Iterable[str]) -> Generator[list[int]]:
    """Parse the input data into lists of integers."""
    for row in data:
        yield [int(level) for level in row.split()]


def is_safe(row: list[int]) -> bool:
    """
    Check if the row is safe.

    A row is safe if it has a continuous incline and a gradual incline.
    """
    has_continuous_incline = row == sorted(row) or row == sorted(row, reverse=True)
    has_gradual_incline = all(MIN_INCLINE <= abs(a - b) <= MAX_INCLINE for a, b in pairwise(row))
    return has_continuous_incline and has_gradual_incline


def solve(data: Iterable[str]) -> int:
    """Compute the number of safe rows."""
    return len(list(filter(is_safe, parse_input(data))))
