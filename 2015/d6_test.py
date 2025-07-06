from d6 import _reset_grid, _reset_grid_2, p1, p2  # type: ignore

p1_inputs = [
    ("turn on 0,0 through 999,999", 1000 * 1000),
    ("toggle 0,0 through 999,0", 1 * 1000),
    ("turn on 499,499 through 500,500", 4),
]

p2_inputs = [("turn on 0,0 through 0,0", 1), ("toggle 0,0 through 999,999", 2000000)]

if __name__ == "__main__":
    for input, expected in p1_inputs:
        _reset_grid()
        try:
            assert expected == p1(input, True)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")

    for input, expected in p2_inputs:
        _reset_grid_2()
        try:
            assert expected == p2(input, True)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")
