from collections.abc import Generator, Iterable
from dataclasses import dataclass, field


class NoStartPointFoundError(Exception):
    """Raised when no start point is found in the grid."""


@dataclass(frozen=True)
class Point:
    """A point in the grid with an x and y coordinate and a symbol."""

    x: int
    y: int
    symbol: str = field(hash=False)


type Direction = tuple[int, int]
type Grid = list[list[Point]]

directions: dict[str, Direction] = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

patrol_order: list[str] = list(directions.keys())


def next_direction(symbol: str) -> str:
    """Return the next direction in the patrol order."""
    index = patrol_order.index(symbol)
    return patrol_order[(index + 1) % len(patrol_order)]


def parse(data: Iterable[str]) -> tuple[Grid, Point]:
    """Parse the input data into a grid and find the start point for the patrol."""
    grid: Grid = []
    start: Point | None = None

    for y, line in enumerate(data):
        row = []
        for x, symbol in enumerate(line.strip("\n")):
            point = Point(x, y, symbol)
            row.append(point)
            if symbol in directions:
                start = point
        grid.append(row)

    if start is None:
        raise NoStartPointFoundError

    return grid, start


def patrol(grid: Grid, start: Point) -> Generator[Point]:
    """
    Patrol the grid starting at the given point.

    The starting point must indicate the direction of the patrol.
    """
    x, y = start.x, start.y
    direction = start.symbol

    while 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        yield grid[y][x]

        dx, dy = directions[direction]

        is_next_in_bounds = 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[y + dy])
        is_next_blocked = is_next_in_bounds and grid[y + dy][x + dx].symbol == "#"

        if is_next_blocked:
            direction = next_direction(direction)
            dx, dy = directions[direction]

        x += dx
        y += dy


def solve(data: Iterable[str]) -> int:
    """Count the number of distinct points visited by the patrol."""
    grid, start = parse(data)
    return len(set(patrol(grid, start)))
