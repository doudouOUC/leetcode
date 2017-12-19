# -*- coding: utf-8 -*-
#
# File Name: test_5.py
# Author: jinye
# mail: jinye.djy@alibaba-inc.com
from unittest import TestCase
from leetcode5 import Solution


# Create Time: 19/12/2017 21:01
class Test5Solution(TestCase):
    def test_longestPalindrome_dp(self):
        solution = Solution()
        substring = solution.longestPalindrome_dp("babad")
        self.assertEqual("ba", substring)
