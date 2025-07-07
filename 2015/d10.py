from typing import List


def look_and_say(line: str) -> str:
    result: List[str] = []
    i = 0

    while i < len(line):
        count = 1
        while i + 1 < len(line) and line[i] == line[i + 1]:
            count += 1
            i += 1
        result.append(f"{str(count)}{line[i]}")
        i += 1

    return "".join(result)


def p1(line: str, iterations: int) -> int:
    temp = line

    for _ in range(iterations):
        temp = look_and_say(temp)

    return len(temp)


if __name__ == "__main__":
    with open("2015/inputs/d10.txt") as f:
        lines = f.read().splitlines()

    print("P1:", p1(lines[0], 40))
    print("P1:", p1(lines[0], 50))
