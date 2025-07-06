from d1 import p1, p2

p1_inputs = [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
]

p2_inputs = [(")", 1), ("()())", 5)]

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
