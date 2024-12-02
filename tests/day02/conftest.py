from collections.abc import Iterable
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def sample_data() -> Iterable[str]:
    """The sample input data."""
    input_path = Path(__file__).parent / "data" / "sample"
    with input_path.open() as f:
        return f.readlines()


@pytest.fixture(scope="session")
def full_data() -> Iterable[str]:
    """The complete input data."""
    input_path = Path(__file__).parent / "data" / "input"
    with input_path.open() as f:
        return f.readlines()
