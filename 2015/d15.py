import re
from typing import Dict, List, Tuple

PATTERN = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"


def parse_line(line: str) -> Tuple[str, Tuple[int, int, int, int, int]]:
    m = re.match(PATTERN, line)
    name, *props = m.groups()  # type: ignore
    return name, tuple(map(int, props))  # type: ignore


def generate_combinations(n: int, total: int) -> List[List[int]]:
    def helper(so_far: List[int], remaining: int) -> List[List[int]]:
        if len(so_far) == n - 1:
            return [so_far + [remaining]]
        combinations = []
        for i in range(remaining + 1):
            combinations += helper(so_far + [i], remaining - i)  # type: ignore
        return combinations  # type: ignore

    return helper([], total)


def p1(lines: List[str]) -> int:
    ingredients: Dict[str, Tuple[int, int, int, int, int]] = {
        name: props for line in lines for name, props in [parse_line(line)]
    }

    best_score = 0
    ingredient_values = list(ingredients.values())

    for amounts in generate_combinations(len(ingredient_values), 100):
        totals = [0, 0, 0, 0]  # capacity, durability, flavour, texture

        for i, (cap, dur, fla, tex, _) in enumerate(ingredient_values):
            totals[0] += cap * amounts[i]
            totals[1] += dur * amounts[i]
            totals[2] += fla * amounts[i]
            totals[3] += tex * amounts[i]

        if any(x <= 0 for x in totals):
            continue

        score = 1
        for val in totals:
            score *= val
        best_score = max(best_score, score)

    return best_score


def p2(lines: List[str], calorie_target: int = 500) -> int:
    ingredients: Dict[str, Tuple[int, int, int, int, int]] = {
        name: props for line in lines for name, props in [parse_line(line)]
    }

    best_score = 0
    ingredient_values = list(ingredients.values())

    for amounts in generate_combinations(len(ingredient_values), 100):
        totals = [0, 0, 0, 0]  # capacity, durability, flavour, texture
        calories = 0

        for i, (cap, dur, fla, tex, cal) in enumerate(ingredient_values):
            totals[0] += cap * amounts[i]
            totals[1] += dur * amounts[i]
            totals[2] += fla * amounts[i]
            totals[3] += tex * amounts[i]
            calories += cal * amounts[i]

        if any(x <= 0 for x in totals) or calories != calorie_target:
            continue

        score = 1
        for val in totals:
            score *= val
        best_score = max(best_score, score)

    return best_score


if __name__ == "__main__":
    with open("2015/inputs/d15.txt") as f:
        lines = f.read().splitlines()

    print(f"P1: {p1(lines)}")
    print(f"P2: {p2(lines)}")
