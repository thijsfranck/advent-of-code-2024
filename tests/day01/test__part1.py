from collections.abc import Iterable
from pathlib import Path

import pytest

from advent_of_code_2024.day01 import part1


@pytest.fixture()
def sample_data() -> Iterable[str]:
    """The sample input data."""
    input_path = Path(__file__).parent / "data" / "sample"
    with input_path.open() as f:
        return f.readlines()


@pytest.fixture()
def full_data() -> Iterable[str]:
    """The complete input data."""
    input_path = Path(__file__).parent / "data" / "input"
    with input_path.open() as f:
        return f.readlines()


@pytest.mark.parametrize(
    ("fixture", "expected"),
    [
        ("sample_data", 11),
        ("full_data", 2367773),
    ],
)
def test__solution(fixture: str, expected: int, request: pytest.FixtureRequest) -> None:
    """
    Test the solution with various inputs.

    Asserts:
        - The solution returns the expected result.
    """
    assert part1.solve(request.getfixturevalue(fixture)) == expected
