import ast
from typing import List, Tuple


def lenx(s: str) -> Tuple[int, int]:
    return len(s), len(ast.literal_eval(s))


def encode(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def p1(lines: List[str]) -> int:
    t_code, t_memory = 0, 0

    for line in lines:
        c, m = lenx(line)

        t_code += c
        t_memory += m

    return t_code - t_memory


def p2(lines: List[str]) -> int:
    t_encoded = 0
    t_orig = 0

    for line in lines:
        e = encode(line)
        t_encoded += len(e)
        t_orig += len(line)

    return t_encoded - t_orig


if __name__ == "__main__":
    with open("2015/inputs/d8.txt") as f:
        lines = f.read().splitlines()

    print("P1:", p1(lines))
    print("P2:", p2(lines))
