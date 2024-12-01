from collections.abc import Iterable


def parse_input(data: Iterable[str]) -> tuple[list[int], list[int]]:
    """Parse the input data into sorted lists of integers."""
    left, right = zip(*(line.split() for line in data), strict=True)
    return sorted(map(int, left)), sorted(map(int, right))


def solve(data: Iterable[str]) -> int:
    """Compute the sum of the absolute differences between the sorted elements of the two lists."""
    return sum(abs(a - b) for a, b in zip(*parse_input(data), strict=True))
