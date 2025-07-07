import re
from itertools import permutations
from typing import List, Tuple, Dict, Set


def parse_line(line: str):
    match = re.match(r"(\w+) to (\w+) = (\d+)", line)
    if match:
        f, t, d = match.groups()
        return f, t, int(d)
    raise ValueError(f"Invalid line: {line}")


def p1(lines: List[str]) -> float:
    d: Dict[Tuple[str, str], int] = {}
    for line in lines:
        f, t, dist = parse_line(line)
        d[(f, t)] = dist
        d[(t, f)] = dist

    locations: Set[str] = set()
    for a, b in d:
        locations.add(a)
        locations.add(b)

    min_total = float("inf")
    for path in permutations(locations):
        total = 0
        for i in range(len(path) - 1):
            total += d[(path[i], path[i + 1])]
        min_total = min(min_total, total)

    return min_total


def p2(lines: List[str]) -> float:
    d: Dict[Tuple[str, str], int] = {}
    for line in lines:
        f, t, dist = parse_line(line)
        d[(f, t)] = dist
        d[(t, f)] = dist

    locations: Set[str] = set()
    for a, b in d:
        locations.add(a)
        locations.add(b)

    max_total = -float("inf")
    for path in permutations(locations):
        total = 0
        for i in range(len(path) - 1):
            total += d[(path[i], path[i + 1])]
        max_total = max(max_total, total)

    return max_total


if __name__ == "__main__":
    with open("2015/inputs/d9.txt") as f:
        lines = f.read().splitlines()

    print("P1:", p1(lines))
    print("P2:", p2(lines))
