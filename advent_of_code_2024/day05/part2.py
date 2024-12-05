from collections import defaultdict
from collections.abc import Iterable
from functools import cmp_to_key

type Index = dict[int, list[int]]
type Update = list[int]


def parse(data: Iterable[str]) -> tuple[Index, Index, list[Update]]:
    """Parse the input data into a multimap of rules (before, after) and a list of updates."""
    before: Index = defaultdict(list)
    after: Index = defaultdict(list)
    updates: list[Update] = []

    state = "rules"

    for line in data:
        content = line.strip("\n")

        if not content:
            state = "updates"
            continue

        if state == "rules":
            a, b = map(int, content.split("|"))
            after[a].append(b)
            before[b].append(a)
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


def order_update(update: Update, before: Index, after: Index) -> Update:
    """Order the given update."""
    return sorted(update, key=cmp_to_key(lambda a, b: -1 if a in before[b] or b in after[a] else 1))


def solve(data: Iterable[str]) -> int:
    """Find the sum of the middle elements of the ordered updates."""
    before, after, updates = parse(data)
    unordered_updates = [update for update in updates if not is_ordered(update, before, after)]
    ordered_updates = [order_update(update, before, after) for update in unordered_updates]
    return sum(update[len(update) // 2] for update in ordered_updates)
