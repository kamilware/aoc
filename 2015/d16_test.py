import unittest
from d16 import parse_ticker_tape, parse_line, p1, p2


class TestDay16(unittest.TestCase):
    def test_parse_ticker_tape(self):
        expected = {
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

        self.assertEqual(parse_ticker_tape(), expected)

    def test_parse_line(self):
        line = "Sue 123: cats: 7, goldfish: 5, perfumes: 1"
        sue_id, traits = parse_line(line)

        self.assertEqual(sue_id, 123)
        self.assertEqual(traits, {"cats": 7, "goldfish": 5, "perfumes": 1})

    def test_p1(self):
        lines = [
            "Sue 1: goldfish: 5, trees: 3, cars: 2",
            "Sue 2: children: 3, samoyeds: 2, perfumes: 1",
            "Sue 3: cats: 7, goldfish: 5, perfumes: 1",
        ]

        self.assertEqual(p1(lines), 1)

    def test_p2(self):
        lines = [
            "Sue 1: cats: 8, trees: 4",
            "Sue 2: pomeranians: 2, goldfish: 4",
            "Sue 3: cats: 7, goldfish: 5",
        ]

        self.assertEqual(p2(lines), 1)


if __name__ == "__main__":
    unittest.main()
