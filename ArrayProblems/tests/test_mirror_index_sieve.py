import unittest

from ArrayProblems.mirror_index_sieve import mirror_sieve


class TestMirrorSieve(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(mirror_sieve([1, 2, 3, 4, 6]), [3])
        self.assertEqual(mirror_sieve([1, 1, 1, 1]), [])
        self.assertEqual(mirror_sieve([2, 5, 2]), [1])

    def test_edge_cases(self):
        self.assertEqual(mirror_sieve([]), [])
        self.assertEqual(mirror_sieve([5]), [0])  # left=0, right=0
        self.assertEqual(mirror_sieve([1, 0, 1]), [1])

    def test_multiple_matches(self):
        # [0, 1, 0] -> i=1: 0 == 0
        self.assertEqual(mirror_sieve([0, 1, 0]), [1])


if __name__ == "__main__":
    unittest.main()
