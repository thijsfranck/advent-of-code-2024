from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def sample_data_part1() -> str:
    """The sample input data."""
    input_path = Path(__file__).parent / "data" / "sample_part1"
    with input_path.open() as f:
        return f.read()


@pytest.fixture(scope="session")
def sample_data_part2() -> str:
    """The sample input data."""
    input_path = Path(__file__).parent / "data" / "sample_part2"
    with input_path.open() as f:
        return f.read()


@pytest.fixture(scope="session")
def full_data() -> str:
    """The complete input data."""
    input_path = Path(__file__).parent / "data" / "input"
    with input_path.open() as f:
        return f.read()
