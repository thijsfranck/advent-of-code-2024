from collections import Counter
from collections.abc import Iterable


def parse_input(data: Iterable[str]) -> tuple[list[int], list[int]]:
    """Parse the input data into lists of integers."""
    left, right = zip(*(line.split() for line in data), strict=True)
    return list(map(int, left)), list(map(int, right))


def solve(data: Iterable[str]) -> int:
    """
    Compute the sum of the similarities between the elements of the two lists.

    The similarity of an element is the product of the element and the number of times it appears in the other list.
    """
    left, right = parse_input(data)
    count = Counter(right)
    return sum(number * count.get(number, 0) for number in left)
