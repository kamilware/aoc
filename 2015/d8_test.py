from d8 import lenx, p1, encode, p2

lenx_inputs = [
    ('""', (2, 0)),
    ('"abc"', (5, 3)),
    ('"aaa\\"aaa"', (10, 7)),
    ('"\\x27"', (6, 1)),
]

p1_input = [x[0] for x in lenx_inputs]
p1_expected = 12

encode_inputs = [
    ('""', '"\\"\\""'),
    ('"abc"', '"\\"abc\\""'),
    ('"aaa\\"aaa"', '"\\"aaa\\\\\\"aaa\\""'),
    ('"\\x27"', '"\\"\\\\x27\\""'),
]

p2_input = [x[0] for x in encode_inputs]
p2_expected = 19

if __name__ == "__main__":
    for input, expected in lenx_inputs:
        try:
            assert expected == lenx(input)
        except AssertionError:
            res = lenx(input)
            print(f"input: {input}, expected: {expected}, got: {res}")

    try:
        assert p1_expected == p1(p1_input)
    except AssertionError:
        print(f"input: {input}, expected: {p1_expected}, got: {p1(p1_input)}")

    for input, expected in encode_inputs:
        try:
            assert expected == encode(input)
        except AssertionError:
            res = encode(input)
            print(f"input: {input}, expected: {expected}, got: {res}")

    try:
        assert p2_expected == p2(p2_input)
    except AssertionError:
        print(f"input: {input}, expected: {p2_input}, got: {p2(p2_input)}")
