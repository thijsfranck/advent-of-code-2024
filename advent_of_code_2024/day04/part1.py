from collections.abc import Generator, Iterable

WORDS = ["XMAS"]

type Point = tuple[int, int]

directions: list[Point] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def parse_matrix(data: Iterable[str]) -> list[str]:
    """Return a matrix from the input data."""
    return list(data)


def find_words_in_direction(matrix: list[str], start: Point, direction: Point) -> Generator[str]:
    """Travel in a direction from a starting point and return any words found."""
    x, y = start
    token = ""

    while 0 <= y < len(matrix) and 0 <= x < len(matrix[y]):
        token += matrix[y][x]

        if token in WORDS:
            yield token

        if not any(word.startswith(token) for word in WORDS):
            return

        x += direction[0]
        y += direction[1]


def find_words(matrix: list[str]) -> Generator[int]:
    """Find all words in the matrix."""
    for y, row in enumerate(matrix):
        for x in range(len(row)):
            for direction in directions:
                yield len(list(find_words_in_direction(matrix, (x, y), direction)))


def solve(data: Iterable[str]) -> int:
    """Find the number of words in the given data."""
    matrix = parse_matrix(data)
    return sum(find_words(matrix))
