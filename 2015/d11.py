import string


LETTERS = list(string.ascii_lowercase)
FORBIDDEN_LETTERS = list("iol")


def has_min_x_pairs(input: str, pairs: int) -> bool:
    count = 0
    i = 0
    while i < len(input) - 1:
        if input[i] == input[i + 1]:
            count += 1
            i += 2
            if count == pairs:
                return True
        else:
            i += 1
    return False


def has_increasing_straight(input: str) -> bool:
    for i in range(len(input) - 2):
        a, b, c = input[i], input[i + 1], input[i + 2]
        if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
            return True
    return False


def contains_a_forbidden_letter(input: str) -> bool:
    return any(c in FORBIDDEN_LETTERS for c in input)


def is_allowed(input: str) -> bool:
    return (
        has_increasing_straight(input)
        and not contains_a_forbidden_letter(input)
        and has_min_x_pairs(input, 2)
    )


def inc_password(input: str) -> str:
    pw = list(input)
    i = len(pw) - 1
    while i >= 0:
        if pw[i] == "z":
            pw[i] = "a"
            i -= 1
        else:
            pw[i] = LETTERS[LETTERS.index(pw[i]) + 1]
            break
    return "".join(pw)


def p1(input: str) -> str:
    pw = input
    while True:
        pw = inc_password(pw)
        if is_allowed(pw):
            return pw


if __name__ == "__main__":
    with open("2015/inputs/d11.txt") as f:
        line = f.read().splitlines()[0]

    print("P1:", pw := p1(line))
    print("P2:", p1(pw))
