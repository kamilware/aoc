FORBIDDEN_STRINGS = "ab, cd, pq, or xy".replace("or", "").replace(" ", "").split(",")


def _has_3_vowels(input: str) -> bool:
    vowels = list("aeiou")

    c = 0
    for ch in input:
        if ch in vowels:
            c += 1

    return c >= 3


def _letter_twice_in_a_row(input: str) -> bool:
    for i in range(len(input)):
        try:
            if input[i] == input[i + 1]:
                return True
        except IndexError:
            return False

    return False


def _contains_forbidden_strings(input: str) -> bool:
    for x in FORBIDDEN_STRINGS:
        if x in input:
            return True

    return False


def _contains_repeating_letter_with_one_letter_between(input: str) -> bool:
    for i in range(len(input)):
        try:
            if input[i] == input[i + 2]:
                return True
        except IndexError:
            return False

    return False


def _contains_pair_no_overlapping(input: str) -> bool:
    for i in range(len(input)):
        try:
            pair = input[i], input[i + 1]
            if f"{pair[0]}{pair[1]}" in "".join(input[i + 2 :]):
                return True
        except IndexError:
            return False

    return False


def p1(input: str) -> bool:
    return (
        not _contains_forbidden_strings(input)
        and _letter_twice_in_a_row(input)
        and _has_3_vowels(input)
    )


def p2(input: str) -> int:
    return _contains_repeating_letter_with_one_letter_between(
        input
    ) and _contains_pair_no_overlapping(input)


if __name__ == "__main__":
    with open("2015/inputs/d5.txt") as f:
        lines = f.readlines()

    p1_res = 0
    for line in lines:
        if p1(line):
            p1_res += 1

    p2_res = 0
    for line in lines:
        if p2(line):
            p2_res += 1

    print(f"P1: {p1_res}")
    print(f"P2: {p2_res}")
