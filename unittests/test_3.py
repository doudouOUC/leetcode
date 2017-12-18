# -*- coding: utf-8 -*-
#
# File Name: test_3.py
# Author: jinye

from unittest import TestCase
from leetcode3 import Solution

# Create Time: 17/12/2017 14:19
class Test3Solution(TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        answer = solution.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual("abc", answer)
        answer = solution.lengthOfLongestSubstring("pwwkew")
        self.assertEqual("wke", answer)
        answer = solution.lengthOfLongestSubstring("bbbbbb")
        self.assertEqual("b", answer)
