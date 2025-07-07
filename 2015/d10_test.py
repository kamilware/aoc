from d10 import look_and_say

parse_line_inputs = [
    ("1", "11"),
    ("11", "21"),
    ("21", "1211"),
    ("1211", "111221"),
    ("111221", "312211"),
]

if __name__ == "__main__":
    try:
        for line, exp in parse_line_inputs:
            assert exp == look_and_say(line)
    except AssertionError:
        print(f"input: {input}")
