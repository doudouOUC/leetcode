# -*- coding: utf-8 -*-
#
# File Name: leetcode5.py
# Author: jinye
# Create Time: 19/12/2017 20:45


class Solution:
    def longestPalindrome_dp(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        start_i = 0
        max_len = 0
        dp = [[False] * length for row in range(length)]
        for i in range(length):
            dp[i][i] = True
            if i+1 < length and s[i] != s[i]:
                dp[i][j+1] = True
        for tmp_len in range(2, length):
            for i in range(length-tmp_len):
                j = i + tmp_len - 1
                if dp[i-1][j+1] and s[i] == s[j]:
                    dp[i][j] = True
                    max_len = tmp_len
                    start_i = i
        sub_string = s[start_i:max_len]
        return sub_string

