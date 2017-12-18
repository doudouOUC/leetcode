# -*- coding: utf-8 -*-
#
# File Name: leetcode4.py
# Author: jinye
# Create Time: 18/12/2017 15:41


class Solution:
    def longestPalindrome_dp(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        p = [[0]*length for row in range(length)]
        