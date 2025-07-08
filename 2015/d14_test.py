from d14 import parse_line

input = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds",
]

parse_line_expected = [{"Comet": (14, 10, 127)}, {"Dancer": (16, 11, 162)}]

if __name__ == "__main__":
    for inp, exp in zip(input, parse_line_expected):
        res = parse_line(inp)
        try:
            assert res == exp
        except AssertionError:
            print(f"1 | input: {input}, expected: {exp}, actual: {res}")
