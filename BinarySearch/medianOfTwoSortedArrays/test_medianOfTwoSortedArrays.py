#! /usr/bin/env python3
import unittest
from medianOfTwoSortedArrays import Solution

class TestTimeMap(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_set_and_get(self):

        self.assertEqual(self.sol.findMedianSortedArrays([1,3], [2]), 2.00000)
        self.assertEqual(self.sol.findMedianSortedArrays([2], [1,3]), 2.00000)
        self.assertEqual(self.sol.findMedianSortedArrays([1,2], [3]), 2.00000)
        self.assertEqual(self.sol.findMedianSortedArrays([1,2], [3,4]), 2.50000)
        


if __name__ == "__main__":
    unittest.main()