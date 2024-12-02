import pytest

from advent_of_code_2024.day02 import part1


@pytest.mark.parametrize(
    ("row", "expected"),
    [
        ([7, 6, 3, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test__is_safe(*, row: list[int], expected: bool) -> None:
    """
    Test the is_safe function.

    Asserts:
        - The function returns the expected result.
    """
    assert part1.is_safe(row) == expected


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("sample_data", 2),
        ("full_data", 242),
    ],
)
def test__solution(fixture: str, expected: int, request: pytest.FixtureRequest) -> None:
    """
    Test the solution with various inputs.

    Asserts:
        - The solution returns the expected result.
    """
    assert part1.solve(request.getfixturevalue(fixture)) == expected
