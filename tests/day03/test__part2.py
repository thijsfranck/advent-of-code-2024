import pytest

from advent_of_code_2024.day03 import part2


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ("mul(44,46)", [2024]),
        ("mul(123,4)", [492]),
        ("mul(4*", []),
        ("mul(6,9!", []),
        ("?(12,34)", []),
        ("mul ( 2 , 4 )", []),
        ("mul( 2 , 4 )", []),
        ("mul(6,9mul(4,20)", [80]),
        ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", [8, 40]),
    ],
)
def test__parser(data: str, expected: int) -> None:
    """
    Test the parser with various inputs.

    Asserts:
        - The function returns the expected result.
    """
    assert list(part2.Parser(data)) == expected


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("sample_data_part2", 48),
        ("full_data", 113965544),
    ],
)
def test__solution(fixture: str, expected: int, request: pytest.FixtureRequest) -> None:
    """
    Test the solution with various inputs.

    Asserts:
        - The solution returns the expected result.
    """
    assert part2.solve(request.getfixturevalue(fixture)) == expected
