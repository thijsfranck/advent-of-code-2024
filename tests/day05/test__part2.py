import pytest

from advent_of_code_2024.day05 import part2


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("sample_data", 123),
        ("full_data", 5346),
    ],
)
def test__solution(fixture: str, expected: int, request: pytest.FixtureRequest) -> None:
    """
    Test the solution with various inputs.

    Asserts:
        - The solution returns the expected result.
    """
    assert part2.solve(request.getfixturevalue(fixture)) == expected
