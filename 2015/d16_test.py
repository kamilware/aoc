from d16 import parse_ticker_tape

parse_ticker_tape_expected = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


if __name__ == "__main__":
    res = parse_ticker_tape()
    try:
        assert parse_ticker_tape_expected == res
    except AssertionError:
        print(
            f"1 | input: {input}, expected: {parse_ticker_tape_expected}, actual: {res}"
        )
