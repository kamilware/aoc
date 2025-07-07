from d7 import p1

p1_input = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i",
], {
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456,
}


if __name__ == "__main__":
    try:
        lines, d = p1_input
        res = p1(lines)
        for key in d:
            assert d[key] == res[key]
    except AssertionError:
        print("incorrect value")
