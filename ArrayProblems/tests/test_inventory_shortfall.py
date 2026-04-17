import unittest

from ArrayProblems.inventory_shortfall import find_smallest_missing_id


class TestInventoryShortfall(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(find_smallest_missing_id([0, 1, 2, 4, 5]), 3)

    def test_example_2(self):
        self.assertEqual(find_smallest_missing_id([1, 2, 3]), 0)

    def test_example_3(self):
        self.assertEqual(find_smallest_missing_id([0, 1, 2, 3, 5]), 4)

    def test_empty_sequence(self):
        # Constraints say 1 <= array.length, but worth checking boundary
        self.assertEqual(find_smallest_missing_id([]), 0)

    def test_no_missing(self):
        self.assertEqual(find_smallest_missing_id([0, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
