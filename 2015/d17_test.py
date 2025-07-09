import unittest
from d17 import parse_input, p1, p2


class TestDay17(unittest.TestCase):
    def setUp(self):
        self.raw = ["20", "15", "10", "5", "5"]
        self.parsed = [20, 15, 10, 5, 5]

    def test_parse_input(self):
        self.assertEqual(parse_input(self.raw), self.parsed)

    def test_p1_example(self):
        self.assertEqual(p1(self.parsed, target=25), 4)

    def test_p2_example(self):
        self.assertEqual(p2(self.parsed, target=25), 3)


if __name__ == "__main__":
    unittest.main()
