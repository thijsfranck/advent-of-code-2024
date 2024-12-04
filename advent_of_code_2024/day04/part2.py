from collections.abc import Generator, Iterable

type Point = tuple[int, int]

WORDS = ["MAS"]

positions: list[tuple[Point, Point]] = [
    ((-1, -1), (1, 1)),
    ((-1, 1), (1, -1)),
]


def parse_matrix(data: Iterable[str]) -> list[str]:
    """Return a matrix from the input data."""
    return list(data)


def is_match(matrix: list[str], start: Point, position: tuple[Point, Point]) -> bool:
    """Check if the given position is a match."""
    x, y = start

    if not all(0 <= y + dy < len(matrix) and 0 <= x + dx < len(matrix[y]) for dx, dy in position):
        return False

    a, b = position

    token = matrix[y + a[1]][x + a[0]] + matrix[y][x] + matrix[y + b[1]][x + b[0]]

    return token in WORDS or token[::-1] in WORDS


def find_xmas(matrix: list[str]) -> Generator[int]:
    """Find all occurrences of x-mas in the matrix."""
    for y, row in enumerate(matrix):
        for x in range(len(row)):
            if all(is_match(matrix, (x, y), position) for position in positions):
                yield 1


def solve(data: Iterable[str]) -> int:
    """Find the number of words in the given data."""
    matrix = parse_matrix(data)
    return sum(find_xmas(matrix))
