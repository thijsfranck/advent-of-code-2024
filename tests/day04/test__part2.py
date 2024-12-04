import pytest

from advent_of_code_2024.day04 import part2


@pytest.mark.parametrize(
    ("pattern", "expected"),
    [
        (
            [
                "M.S",
                ".A.",
                "M.S",
            ],
            1,
        ),
        (
            [
                "M.M",
                ".A.",
                "S.S",
            ],
            1,
        ),
        (
            [
                "S.S",
                ".A.",
                "M.M",
            ],
            1,
        ),
        (
            [
                "S.M",
                ".A.",
                "S.M",
            ],
            1,
        ),
    ],
)
def test__find_xmas(pattern: list[str], expected: int) -> None:
    """
    Test the find_xmas function with various inputs.

    Asserts:
        - The function returns the expected number of matches.
    """
    assert sum(part2.find_xmas(pattern)) == expected


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("sample_data", 9),
        ("full_data", 1992),
    ],
)
def test__solution(fixture: str, expected: int, request: pytest.FixtureRequest) -> None:
    """
    Test the solution with various inputs.

    Asserts:
        - The solution returns the expected result.
    """
    assert part2.solve(request.getfixturevalue(fixture)) == expected
