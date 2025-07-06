from d2 import p1, p2

p1_inputs = [
    ("2x3x4", 58),
    ("1x1x10", 43),
]

p2_inputs = [("2x3x4", 34), ("1x1x10", 14)]

if __name__ == "__main__":
    for input, expected in p1_inputs:
        try:
            assert expected == p1(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p2_inputs:
        try:
            assert expected == p2(input)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")
