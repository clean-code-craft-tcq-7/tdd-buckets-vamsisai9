import unittest
import tdd_range 

class TestGetRanges(unittest.TestCase):
    def test_single_range(self):
        samples = [4, 5]
        expected = [("4-5", 2)]
        self.assertEqual(tdd_range.get_ranges(sorted(samples)), expected)

    def test_multiple_ranges(self):
        samples = [3, 4, 5, 10, 11, 12]
        expected = [("3-5", 3), ("10-12", 3)]
        self.assertEqual(tdd_range.get_ranges(sorted(samples)), expected)

    def test_single_sample(self):
        samples = [3]
        expected = []
        self.assertEqual(tdd_range.get_ranges(sorted(samples)), expected)

if __name__ == '__main__':
    unittest.main()
