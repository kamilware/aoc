import re
import json
from typing import Any


def p1(input: str) -> int:
    numbers = re.findall(r"-?\d+", input)
    return sum(map(int, numbers))


def p2(input: str) -> int:
    def sum_json(obj: Any) -> int:
        if isinstance(obj, int):
            return obj
        elif isinstance(obj, list):
            return sum(sum_json(x) for x in obj)  # type: ignore
        elif isinstance(obj, dict):
            if "red" in obj.values():
                return 0
            return sum(sum_json(v) for v in obj.values())  # type: ignore
        return 0

    data = json.loads(input)
    return sum_json(data)


if __name__ == "__main__":
    with open("2015/inputs/d12.txt") as f:
        line: str = f.read().strip()

    print(f"P1: {p1(line)}")
    print(f"P2: {p2(line)}")
