def p1(input: str) -> int:
    l, w, h = [int(x) for x in input.split("x")]
    sides = [l * w, w * h, h * l]

    return sum(2 * x for x in sides) + min(sides)


def p2(input: str) -> int:
    s = [int(x) for x in input.split("x")]
    s.sort()

    return 2 * s[0] + 2 * s[1] + s[0] * s[1] * s[2]


if __name__ == "__main__":
    with open("2015/inputs/d2.txt") as f:
        lines = f.readlines()

    p1_res = 0
    for line in lines:
        p1_res += p1(line)

    p2_res = 0
    for line in lines:
        p2_res += p2(line)

    print(f"P1: {p1_res}")
    print(f"P2: {p2_res}")
