import re
from typing import Dict, List, Tuple

LINE_RE = r"(\w+): (\d+)"
TICKER_TAPE_RE = r"(\w+): (\d+)"
TICKER_TAPE = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""


def parse_ticker_tape() -> Dict[str, int]:
    result = {}
    for line in TICKER_TAPE.splitlines():
        m = re.match(TICKER_TAPE_RE, line)
        if m:
            key, value = m.groups()
            result[key] = int(value)

    return result  # type: ignore


def parse_line(line: str) -> Tuple[int, Dict[str, int]]:
    match = re.match(r"^Sue (\d+): (.+)$", line)
    if not match:
        raise ValueError(f"Invalid line: {line}")

    sue_id = int(match.group(1))
    s = match.group(2)

    traits = {}
    for part in s.split(", "):
        m = re.match(LINE_RE, part)
        if m:
            key, value = m.groups()
            traits[key] = int(value)

    return sue_id, traits  # type: ignore


def p1(lines: List[str]) -> int:
    ticker = parse_ticker_tape()
    for line in lines:
        sue_id, traits = parse_line(line)
        if all(ticker.get(k) == v for k, v in traits.items()):
            return sue_id

    return -1  # fallback


def p2(lines: List[str]) -> int:
    ticker = parse_ticker_tape()
    for line in lines:
        sue_id, traits = parse_line(line)
        match = True
        for k, v in traits.items():
            if k in ("cats", "trees"):
                if v <= ticker[k]:
                    match = False
                    break
            elif k in ("pomeranians", "goldfish"):
                if v >= ticker[k]:
                    match = False
                    break
            else:
                if v != ticker[k]:
                    match = False
                    break
        if match:
            return sue_id
    return -1


if __name__ == "__main__":
    with open("2015/inputs/d16.txt") as f:
        lines = f.read().splitlines()

    print(f"P1: {p1(lines)}")
    print(f"P2: {p2(lines)}")
