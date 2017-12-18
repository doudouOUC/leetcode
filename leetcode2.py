# -*- coding: utf-8 -*-
#
# File Name: 2.py.py
# Author: jinye

# Create Time: 16/12/2017 16:30


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = self.list2num(l1) + self.list2num(l2)
        list_node = self.num2list(num)
        return list_node

    def num2list(self, num):
        first_num = num % 10
        first_node = ListNode(first_num)
        last_node = first_node
        num = num / 10
        while num != 0:
            next_num = num % 10
            num = num / 10
            next_node = ListNode(next_num)
            last_node.next = next_node
            last_node = next_node
        return first_node

    def list2num(self, list_node):
        num = 0
        multi = 10
        i = 0
        while list_node is not None:
            num += list_node.val * (multi ** i)
            i += 1
            list_node = list_node.next
        return num