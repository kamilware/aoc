import re
from typing import Optional, Tuple, Dict, List


instruction_pattern = re.compile(
    r"""
    (?:(?P<n1>\w+)\s
    (?P<op>AND|OR|LSHIFT|RSHIFT)\s
    (?P<n2>\w+)|
    (?P<op_unary>NOT)\s(?P<n1_unary>\w+)|
    (?P<val_only>\w+))
    \s*->\s*(?P<target>\w+)
    """,
    re.VERBOSE,
)


def parse_line(line: str) -> Tuple[str, str, Optional[str], str]:
    line = line.strip()
    match = instruction_pattern.fullmatch(line)
    if not match:
        raise ValueError(f"Invalid instruction line: {line}")
    groups = match.groupdict()

    if groups["op"]:
        return (
            groups["op"],
            groups["n1"],
            groups["n2"],
            groups["target"],
        )
    elif groups["op_unary"]:
        return (
            groups["op_unary"],
            groups["n1_unary"],
            None,
            groups["target"],
        )
    else:
        return (
            "SET",
            groups["val_only"],
            None,
            groups["target"],
        )


def p1(lines: List[str]) -> Dict[str, int]:
    circuit: Dict[str, Tuple[str, str, Optional[str]]] = {}
    cache: Dict[str, int] = {}

    for line in lines:
        op, n1, n2, target = parse_line(line)
        circuit[target] = (op, n1, n2)

    def get_val(x: str) -> int:
        if x.isdigit():
            return int(x)
        if x in cache:
            return cache[x]

        op, n1, n2 = circuit[x]

        if op == "SET":
            val = get_val(n1)
        elif op == "AND" and n2:
            val = get_val(n1) & get_val(n2)
        elif op == "OR" and n2:
            val = get_val(n1) | get_val(n2)
        elif op == "LSHIFT" and n2:
            val = get_val(n1) << int(n2)
        elif op == "RSHIFT" and n2:
            val = get_val(n1) >> int(n2)
        elif op == "NOT":
            val = ~get_val(n1)

        cache[x] = val & 0xFFFF  # type: ignore
        return cache[x]

    for wire in circuit.keys():
        get_val(wire)

    return cache


def p2(lines: List[str]) -> int:
    orig_vals = p1(lines)
    a = orig_vals["a"]

    new_lines = [line for line in lines if not line.strip().endswith("-> b")]
    new_lines.append(f"{a} -> b")

    return p1(new_lines)["a"]


if __name__ == "__main__":
    with open("2015/inputs/d7.txt") as f:
        lines: List[str] = f.read().splitlines()

    p1_res = p1(lines)["a"]
    print(f"P1: {p1_res}")

    p2_res = p2(lines)
    print(f"P2: {p2_res}")
