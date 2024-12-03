from collections.abc import Generator
from dataclasses import dataclass, field
from enum import IntEnum, auto

NUM_ARGUMENTS = 2
MAX_PARAM_LENGTH = 3


class State(IntEnum):
    """Enum for the state of the current position."""

    OPERATOR = auto()
    PARAMS = auto()


@dataclass
class Parser:
    """Parse the given data and yield the result of the operations found."""

    data: str

    operator: str = ""
    param: str = ""
    params: list[int] = field(default_factory=list)
    state: State = State.OPERATOR

    def __iter__(self) -> Generator[int]:
        operators = {
            "mul": self.mul,
        }

        for char in self.data:
            if self.state == State.PARAMS:
                if char == ")":
                    if 0 < len(self.param) <= MAX_PARAM_LENGTH:
                        self.params.append(int(self.param))

                    yield operators[self.operator]()

                    self.operator = ""
                    self.param = ""
                    self.params.clear()
                    self.state = State.OPERATOR

                    continue

                if char == "," and 0 < len(self.param) <= MAX_PARAM_LENGTH:
                    self.params.append(int(self.param))
                    self.param = ""
                    continue

                self.param += char

                try:
                    int(self.param)
                except ValueError:
                    self.operator = ""
                    self.param = ""
                    self.params.clear()
                    self.state = State.OPERATOR

            if self.state == State.OPERATOR:
                if char == "(" and self.operator in operators:
                    self.state = State.PARAMS
                    continue

                self.operator += char

                if any(op.startswith(self.operator) for op in operators):
                    continue

                self.operator = ""

    def mul(self) -> int:
        """Multiply all the given arguments."""
        if len(self.params) != NUM_ARGUMENTS:
            return 0

        result = 1

        for num in self.params:
            result *= num

        return result


def solve(data: str) -> int:
    """Compute the total of all multiplications in the given data."""
    return sum(Parser(data))
