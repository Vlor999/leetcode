#! /usr/bin/env python3
import unittest
from bestTimeToBuyAndSellStock import Solution

class TestBestTimeBuyAndSell(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_benef(self):
        
        self.assertEqual(self.sol.maxProfit([10,1,5,6,7,1]), 6)
        self.assertEqual(self.sol.maxProfit([10,8,7,5,2]), 0)


if __name__ == "__main__":
    unittest.main()