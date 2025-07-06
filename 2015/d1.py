def p1(input: str) -> int:
    floor = 0

    for c in input:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

    return floor


def p2(input: str) -> int:
    floor = 0
    step = 0

    for c in input:
        step += 1

        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

        if floor < 0:
            return step

    return -1  # in edge case santa does not enter the basement


if __name__ == "__main__":
    with open("2015/inputs/d1.txt") as f:
        line = f.readlines()[0]

    p1_res = p1(line)
    p2_res = p2(line)

    print(f"P1: {p1_res}")
    print(f"P2: {p2_res}")
