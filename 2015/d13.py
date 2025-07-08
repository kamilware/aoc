from itertools import permutations
import re
from typing import Dict, Tuple, List


def parse_input(lines: List[str]):
    happiness: Dict[Tuple[str, str], int] = {}
    for line in lines:
        m = re.match(
            r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.",
            line,
        )

        if m:
            person1, gain_or_lose, units, person2 = m.groups()
            value = int(units) if gain_or_lose == "gain" else -int(units)
            happiness[(person1, person2)] = value

    return happiness


def total_happiness(
    seating: Tuple[str, ...], happiness: Dict[Tuple[str, str], int]
) -> int:
    total = 0
    n = len(seating)
    for i in range(n):
        a, b = seating[i], seating[(i + 1) % n]
        total += happiness.get((a, b), 0) + happiness.get((b, a), 0)

    return total


def p1(lines: List[str]) -> int:
    happiness = parse_input(lines)
    people = set(a for a, _ in happiness.keys())

    return max(total_happiness(p, happiness) for p in permutations(people))


def p2(lines: List[str]) -> int:
    happiness = parse_input(lines)
    people = set(a for a, _ in happiness.keys())
    for person in people:
        happiness[("Me", person)] = 0
        happiness[(person, "Me")] = 0

    people.add("Me")

    return max(total_happiness(p, happiness) for p in permutations(people))


if __name__ == "__main__":
    with open("2015/inputs/d13.txt") as f:
        lines = f.read().splitlines()

    print(f"P1: {p1(lines)}")
    print(f"P2: {p2(lines)}")
