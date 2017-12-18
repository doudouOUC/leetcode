# -*- coding: utf-8 -*-
#
# File Name: leetcode3.py
# Author: jinye

# Create Time: 17/12/2017 14:18


class Solution:
    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pwwkew
        longest = []
        for i in range(len(s)):
            temp = [s[i]]
            for j in range(i+1, len(s)):
                # if s[j] != s[i]:
                flag = 1
                for k in range(len(temp)):
                    if s[j] == temp[k]:
                        flag = 0
                        break
                if flag:
                    temp.append(s[j])
                else:
                    break
            if len(temp) > len(longest):
                longest = temp
        longest = "".join(longest)
        return longest

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pwwkew
        substrings = None
        longest = set()
        i = 0
        j = 0
        ans = 0
        length = len(s)
        while i < length and j < length:
            if s[j] not in longest:
                longest.add(s[j])
                j += 1
                if ans < j-i:
                    ans = j-i
                    substrings = s[i:j]
            else:
                longest.remove(s[i])
                i += 1
        return substrings
