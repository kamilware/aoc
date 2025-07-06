import re
from typing import Optional


def _reset_grid():
    global grid

    grid = [["-" for _ in range(1000)] for _ in range(1000)]


def _reset_grid_2():
    global grid_2

    grid_2 = [[0 for _ in range(1000)] for _ in range(1000)]


grid = [["-" for _ in range(1000)] for _ in range(1000)]
grid_2 = [[0 for _ in range(1000)] for _ in range(1000)]


def _turn_on():
    return "+"


def _turn_on_2(y: int, x: int):
    global grid_2

    grid_2[y][x] += 1


def _toggle(val: str):
    if val == "+":
        return "-"

    return "+"


def _toggle_2(y: int, x: int):
    global grid_2

    grid_2[y][x] += 2


def _turn_off():
    return "-"


def _turn_off_2(y: int, x: int):
    global grid_2

    grid_2[y][x] = max(grid_2[y][x] - 1, 0)


def p1(input: str, return_count: bool = False) -> Optional[int]:
    match = re.search(r"(\d+),(\d+)\s+through\s+(\d+),(\d+)", input)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())

    for y in range(y1, y2 + 1):  # type: ignore
        for x in range(x1, x2 + 1):  # type: ignore
            if "turn on" in input:
                grid[y][x] = _turn_on()
            elif "toggle" in input:
                grid[y][x] = _toggle(grid[y][x])
            elif "turn off" in input:
                grid[y][x] = _turn_off()

    if return_count:
        lit = 0
        for r in grid:
            lit += "".join(r).count("+")
        return lit


def p2(input: str, return_brightness: bool = False) -> Optional[int]:
    match = re.search(r"(\d+),(\d+)\s+through\s+(\d+),(\d+)", input)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())

    for y in range(y1, y2 + 1):  # type: ignore
        for x in range(x1, x2 + 1):  # type: ignore
            if "turn on" in input:
                _turn_on_2(y, x)
            elif "toggle" in input:
                _toggle_2(y, x)
            elif "turn off" in input:
                _turn_off_2(y, x)

    if return_brightness:
        brigthness = 0
        for r in grid_2:
            brigthness += sum(r)
        return brigthness


if __name__ == "__main__":
    _reset_grid()
    _reset_grid_2()

    with open("2015/inputs/d6.txt") as f:
        lines = f.readlines()

    for line in lines:
        p1(line)
        p2(line)

    p1_lit = 0
    for r in grid:
        p1_lit += "".join(r).count("+")

    p2_brigthness = 0
    for r in grid_2:
        p2_brigthness += sum(r)

    print(f"P1: {p1_lit}")
    print(f"P2: {p2_brigthness}")
