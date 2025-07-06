from d4 import p1, p2

p1_inputs = [("abcdef", 5, 609043), ("pqrstuv", 5, 1048970)]

p2_inputs = [("abcdef", 6, 609043), ("pqrstuv", 6, 1048970)]

if __name__ == "__main__":
    for input, zeroes, expected in p1_inputs:
        try:
            assert expected == p1(input, zeroes)
        except AssertionError:
            print(f"input: {input}, zeroes: {zeroes}, expected: {expected}")

    for input, zeroes, expected in p2_inputs:
        try:
            assert expected < p2(input, zeroes)
        except AssertionError:
            print(f"input: {input}, expected: {expected}")
