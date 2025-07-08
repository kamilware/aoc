from d11 import has_increasing_straight, contains_a_forbidden_letter
from d11 import has_min_x_pairs, inc_password, is_allowed, p1

has_increasing_straight_inputs = [("hijklmmn", True), ("abbceffg", False)]
contains_a_forbidden_letter_inputs = [
    ("hijklmmn", True),
    ("abbceffg", False),
    ("abbcegjk", False),
]
has_min_pairs_inputs = [
    ("hijklmmn", 1, True),
    ("hijklmmn", 2, False),
    ("abbcegjk", 1, True),
    ("abbcegjk", 2, False),
    ("abbceffg", 2, True),
]

inc_password_inputs = [("abcdefgh", "abcdefgi"), ("ghijklmn", "ghijklmo")]
is_allowed_inputs = [
    ("hijklmmn", False),
    ("abbceffg", False),
    ("abbcegjk", False),
    ("abcdffaa", True),
    ("ghjaabcc", True),
]
p1_inputs = [("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc")]

if __name__ == "__main__":
    for input, exp in has_increasing_straight_inputs:
        res = has_increasing_straight(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"1 | input: {input}, expected: {exp}, actual: {res}")

    for input, exp in contains_a_forbidden_letter_inputs:
        res = contains_a_forbidden_letter(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"2 | input: {input}, expected: {exp}, actual: {res}")

    for input, pairs, exp in has_min_pairs_inputs:
        res = has_min_x_pairs(input, pairs)
        try:
            assert exp == res
        except AssertionError:
            print(f"4 | input: {input}, expected: {exp}, actual: {res}")

    for input, exp in inc_password_inputs:
        res = inc_password(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"5 | input: {input}, expected: {exp}, actual: {res}")

    for input, exp in is_allowed_inputs:
        res = is_allowed(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"6 | input: {input}, expected: {exp}, actual: {res}")

    for input, exp in p1_inputs:
        res = p1(input)
        try:
            assert exp == res
        except AssertionError:
            print(f"7 | input: {input}, expected: {exp}, actual: {res}")
