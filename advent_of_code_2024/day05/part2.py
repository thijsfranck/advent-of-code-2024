from collections import defaultdict
from collections.abc import Iterable
from graphlib import TopologicalSorter

type Graph = dict[int, set[int]]
type Update = list[int]


def parse(data: Iterable[str]) -> tuple[Graph, list[Update]]:
    """Parse the input data into a multimap of rules (before, after) and a list of updates."""
    graph: Graph = defaultdict(set)
    updates: list[Update] = []

    state = "rules"

    for line in data:
        content = line.strip("\n")

        if not content:
            state = "updates"
            continue

        if state == "rules":
            a, b = map(int, content.split("|"))
            graph[b].add(a)
        else:
            updates.append([int(x) for x in content.split(",")])

    return graph, updates


def order_update(update: Update, graph: Graph) -> Update:
    """Order the given update according to the given graph."""
    subset = set(update)
    sorter = TopologicalSorter({k: v & subset for k, v in graph.items() if k in subset})
    return list(sorter.static_order())


def solve(data: Iterable[str]) -> int:
    """Find the sum of the middle elements of the ordered updates."""
    graph, updates = parse(data)
    ordered_updates = [ordered for update in updates if (ordered := order_update(update, graph)) != update]
    return sum(update[len(update) // 2] for update in ordered_updates)
