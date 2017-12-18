# -*- coding: utf-8 -*-
#
# File Name: test_2.py
# Author: jinye

from unittest import TestCase
from leetcode2 import Solution


# Create Time: 16/12/2017 16:38
class Test2Solution(TestCase):
    def test_addTwoNumbers(self):
        # [2, 4, 3]
        # [5, 6, 4]
        solution = Solution()
        node1 = solution.num2list(342)
        node2 = solution.num2list(465)
        res = solution.addTwoNumbers(node1, node2)

    def test_num2list(self):
        num = 807
        solution = Solution()
        node = solution.num2list(num)
        res = [7, 0, 8]
        i = 0
        while node is not None:
            self.assertEqual(res[i], node.val)
            node = node.next
            i += 1

    def test_list2num(self):
        solution = Solution()
        node = solution.num2list(807)
        num = solution.list2num(node)
        self.assertEqual(807, num)
