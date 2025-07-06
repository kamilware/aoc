import hashlib


def p1(input: str, zeroes: int) -> int:
    prefix = [str(0) for _ in range(zeroes)]
    prefix = "".join(prefix)

    n = 0
    while True:
        x = hashlib.md5(f"{input}{n}".encode())
        x = x.hexdigest()
        if x.startswith(prefix):
            break

        n += 1

    return n


def p2(input: str, zeroes: int) -> int:
    prefix = [str(0) for _ in range(zeroes)]
    prefix = "".join(prefix)

    # n = 254575 # quicker search
    n = 0
    while True:
        x = hashlib.md5(f"{input}{n}".encode())
        x = x.hexdigest()
        if x.startswith(prefix):
            break

        n += 1

    return n


if __name__ == "__main__":
    with open("2015/inputs/d4.txt") as f:
        lines = f.readlines()

    p1_res = 0
    for line in lines:
        p1_res += p1(line, 5)

    p2_res = 0
    for line in lines:
        p2_res += p2(line, 6)

    print(f"P1: {p1_res}")
    print(f"P2: {p2_res}")
