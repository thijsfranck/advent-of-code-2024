import pytest

from advent_of_code_2024.day03 import part1


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
        ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", [8, 25, 88, 40]),
    ],
)
def test__parser(data: str, expected: int) -> None:
    """
    Test the parser with various inputs.

    Asserts:
        - The function returns the expected result.
    """
    assert list(part1.Parser(data)) == expected


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("sample_data_part1", 161),
        ("full_data", 188192787),
    ],
)
def test__solution(fixture: str, expected: int, request: pytest.FixtureRequest) -> None:
    """
    Test the solution with various inputs.

    Asserts:
        - The solution returns the expected result.
    """
    assert part1.solve(request.getfixturevalue(fixture)) == expected
