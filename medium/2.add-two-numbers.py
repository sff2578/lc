#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (40.89%)
# Likes:    29644
# Dislikes: 5775
# Total Accepted:    4.2M
# Total Submissions: 10M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#
# Constraints:
#
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
#
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # reverse 2 lists respectively, then add
        # l1 = self.reverseList(l1)
        # l2 = self.reverseList(l2)
        # self.printList(l1)
        # self.printList(l2)
        # 1 2 9
        # 1 2 3 4
        # 3 6 4 1
        new_head, carry = ListNode(0, None), 0
        cur = new_head
        while l1 != None and l2 != None:
            add_res = l1.val + l2.val + carry
            if add_res >= 10:
                carry = 1
                add_res -= 10
            else:
                carry = 0
            new_ln = ListNode(add_res, None)
            cur.next = new_ln
            cur = new_ln
            l1, l2 = l1.next, l2.next
        tmp = None
        if l1 != None:
            tmp = l1
        else:
            tmp = l2
        while tmp != None:
            add_res = tmp.val + carry
            if add_res >= 10:
                carry = 1
                add_res -= 10
            else:
                carry = 0
            new_ln = ListNode(add_res, None)
            cur.next = new_ln
            cur = cur.next
            tmp = tmp.next

        if carry == 1:
            new_ln = ListNode(1, None)
            cur.next = new_ln
            cur = cur.next
        return new_head.next

    def reverseList(self, head):
        if head.next is None:
            return head
        elif head.next.next is None:
            new_head = head.next
            head.next = None
            new_head.next = head
            return new_head
        tmp1, tmp2 = head.next, head.next.next
        head.next = None
        while True:
            tmp1.next = head
            head = tmp1
            if tmp2 is None:
                break
            tmp1 = tmp2
            tmp2 = tmp1.next
        return head

    def printList(self, head):
        t = head
        while t is not None:
            print(t.val)
            t = t.next
        print("DONE")


# @lc code=end
