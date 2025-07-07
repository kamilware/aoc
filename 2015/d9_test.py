from d9 import parse_line, p1, p2

parse_line_inputs = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141",
]
parse_line_expected = {
    ("London", "Dublin"): 464,
    ("Dublin", "London"): 464,
    ("London", "Belfast"): 518,
    ("Belfast", "London"): 518,
    ("Dublin", "Belfast"): 141,
    ("Belfast", "Dublin"): 141,
}

p1_expected = 605
p2_expected = 982

if __name__ == "__main__":
    d = {}
    for input in parse_line_inputs:
        f, t, dist = parse_line(input)  # type: ignore
        d[(f, t)] = dist
        d[(t, f)] = dist

    try:
        for key in parse_line_expected:
            assert parse_line_expected[key] == d[key]
    except AssertionError:
        print(f"input: {input}, expected: {parse_line_expected}, got: {d}")

    try:
        assert p1(parse_line_inputs) == p1_expected
    except AssertionError:
        print(f"input: {input}, expected: {p1_expected}, got: {d}")

    try:
        assert p2(parse_line_inputs) == p2_expected
    except AssertionError:
        print(f"input: {input}, expected: {p2_expected}, got: {d}")
