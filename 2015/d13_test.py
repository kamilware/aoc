from d13 import p1, p2

input = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol.",
]

p1_expected = 330
p2_expected = 286

if __name__ == "__main__":
    res = p1(input)
    try:
        assert res == p1_expected
    except AssertionError:
        print(f"1 | input: {input}, expected: {p1_expected}, actual: {res}")

    res = p2(input)
    try:
        assert res == p2_expected
    except AssertionError:
        print(f"2 | input: {input}, expected: {p2_expected}, actual: {res}")
