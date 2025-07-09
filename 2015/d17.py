from typing import List
from itertools import combinations


def parse_input(lines: List[str]) -> List[int]:
    return [int(line.strip()) for line in lines if line.strip()]


def p1(containers: List[int], target: int = 150) -> int:
    count = 0
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                count += 1

    return count


def p2(containers: List[int], target: int = 150) -> int:
    valid_combos = [
        combo
        for r in range(1, len(containers) + 1)
        for combo in combinations(containers, r)
        if sum(combo) == target
    ]
    if not valid_combos:
        return 0
    min_len = min(len(c) for c in valid_combos)

    return sum(1 for c in valid_combos if len(c) == min_len)


if __name__ == "__main__":
    with open("2015/inputs/d17.txt") as f:
        containers = parse_input(f.readlines())

    print(f"P1: {p1(containers)}")
    print(f"P2: {p2(containers)}")
