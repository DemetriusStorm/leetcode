"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s_l1 = ''
        s_l2 = ''

        while l1:
            # s_l1 = '{0}{1}'.format(s_l1, str(l1.val))
            s_l1 += str(l1.val)
            l1 = l1.next
        while l2:
            # s_l2 = '{0}{1}'.format(s_l2, str(l2.val))
            s_l2 += str(l2.val)
            l2 = l2.next

        _sum = str(int(s_l1[::-1]) + int(s_l2[::-1]))
        head = tail = ListNode(0)

        for ch in _sum[::-1]:
            cur = ListNode(ch)
            tail.next = cur
            tail = cur

        return head.next


a = Solution()
print(a.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
