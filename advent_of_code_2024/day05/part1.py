from collections import defaultdict
from collections.abc import Iterable

type Index = dict[int, set[int]]
type Update = list[int]


def parse(data: Iterable[str]) -> tuple[Index, Index, list[Update]]:
    """Parse the input data into a multimap of rules (before, after) and a list of updates."""
    before: Index = defaultdict(set)
    after: Index = defaultdict(set)
    updates: list[Update] = []

    state = "rules"

    for line in data:
        content = line.strip("\n")

        if not content:
            state = "updates"
            continue

        if state == "rules":
            a, b = map(int, content.split("|"))
            after[a].add(b)
            before[b].add(a)
        else:
            updates.append([int(x) for x in content.split(",")])

    return before, after, updates


def is_ordered(update: Update, before: Index, after: Index) -> bool:
    """Check if the given update is ordered correctly."""
    for i, x in enumerate(update):
        remaining = update[i + 1 :]
        for y in remaining:
            if x not in before[y] and y not in after[x]:
                return False
    return True


def solve(data: Iterable[str]) -> int:
    """Find the sum of the middle elements of the ordered updates."""
    before, after, updates = parse(data)
    ordered_updates = [update for update in updates if is_ordered(update, before, after)]
    return sum(update[len(update) // 2] for update in ordered_updates)
