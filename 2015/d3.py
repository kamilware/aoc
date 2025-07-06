DIR_MAP = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def p1(input: str) -> int:
    y, x = 0, 0
    visited = {(x, y): 1}

    for c in input:
        y_ch, x_ch = DIR_MAP[c]

        y, x = y + y_ch, x + x_ch
        visited[(x, y)] = visited.get((x, y), 0) + 1

    return len(visited.values())


def p2(input: str) -> int:
    sy, sx = 0, 0
    rsy, rsx = 0, 0
    visited = {(sx, sy): 1}

    for step, c in enumerate(input):
        y_ch, x_ch = DIR_MAP[c]

        if step % 2 == 0:
            # lets go santa
            sy, sx = sy + y_ch, sx + x_ch
            visited[(sx, sy)] = visited.get((sx, sy), 0) + 1
        else:
            rsy, rsx = rsy + y_ch, rsx + x_ch
            visited[(rsx, rsy)] = visited.get((rsx, rsy), 0) + 1

    return len(visited.values())


if __name__ == "__main__":
    with open("2015/inputs/d3.txt") as f:
        lines = f.readlines()

    p1_res = 0
    for line in lines:
        p1_res += p1(line)

    p2_res = 0
    for line in lines:
        p2_res += p2(line)

    print(f"P1: {p1_res}")
    print(f"P2: {p2_res}")
