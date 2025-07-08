from d15 import parse_line

input_lines = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
]

parse_line_expected = [
    ("Butterscotch", (-1, -2, 6, 3, 8)),
    ("Cinnamon", (2, 3, -2, -1, 3)),
]

if __name__ == "__main__":
    for inp, (expected_name, expected_props) in zip(input_lines, parse_line_expected):
        result = parse_line(inp)
        try:
            assert result == (expected_name, expected_props)
        except AssertionError:
            print(
                f"1 | input: {input}, expected: {result}, actual: {(expected_name, expected_props)}"
            )
