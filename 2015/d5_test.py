from d5 import _has_3_vowels, _letter_twice_in_a_row, _contains_forbidden_strings  # type: ignore
from d5 import _contains_repeating_letter_with_one_letter_between, _contains_pair_no_overlapping  # type: ignore
from d5 import p1, p2

p1_inputs_3vowels = [
    ("aei", True),
    ("xazegov", True),
    ("aeiouaeiouaeiou", True),
    ("oew", False),
]

p1_inputs_letter_twice_in_a_row = [
    ("xx", True),
    ("abcdde", True),
    ("aabbccdd", True),
    ("wsef", False),
]

p1_inputs_contains_forbidden_strings = [
    ("ab", True),
    ("abcdde", True),
    ("aabbcpqcdd", True),
    ("wsxyef", True),
    ("wegfgrtgf", False),
]

p1_inputs = [
    ("ugknbfddgicrmopn", True),
    ("aaa", True),
    ("jchzalrnumimnmhp", False),
    ("haegwjzuvuyypxyu", False),
    ("dvszwmarrgswjxmb", False),
]

p2_inputs_contains_repeating_letter_with_one_letter_between = [
    ("xyx", True),
    ("abcdefeghi", True),
    ("aaa", True),
    ("awe", False),
]

p2_inputs_contains_pair_no_overlapping = [
    ("xyxy", True),
    ("aabcdefgaa", True),
    ("aaa", False),
]

p2_inputs = [
    ("qjhvhtzxzqqjkmpb", True),
    ("xxyxx", True),
    ("uurcxstgmygtbstg", False),
    ("ieodomkazucvgmuy", False),
]

if __name__ == "__main__":
    for input, expected in p1_inputs_3vowels:
        try:
            assert expected == _has_3_vowels(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p1_inputs_letter_twice_in_a_row:
        try:
            assert expected == _letter_twice_in_a_row(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p1_inputs_contains_forbidden_strings:
        try:
            assert expected == _contains_forbidden_strings(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p1_inputs:
        try:
            assert expected == p1(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p2_inputs_contains_repeating_letter_with_one_letter_between:
        try:
            assert expected == _contains_repeating_letter_with_one_letter_between(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p2_inputs_contains_pair_no_overlapping:
        try:
            assert expected == _contains_pair_no_overlapping(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p2_inputs:
        try:
            assert expected == p2(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")
