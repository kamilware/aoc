from d3 import p1, p2

p1_inputs = [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)]

p2_inputs = [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)]

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
