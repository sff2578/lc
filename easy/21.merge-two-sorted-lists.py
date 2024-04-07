#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (62.95%)
# Likes:    19332
# Dislikes: 1798
# Total Accepted:    3.4M
# Total Submissions: 5.4M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        retList = ListNode()
        ret = retList
        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                ret.next = node1
                node1 = node1.next
            else:
                ret.next = node2
                node2 = node2.next
            ret = ret.next
        while node1 != None:
            ret.next = node1
            node1 = node1.next
            ret = ret.next
        while node2 != None:
            ret.next = node2
            node2 = node2.next
            ret = ret.next
        return retList.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 04/03/2024
        head = ListNode()
        tmp = head
        while list1 and list2:
            if list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        if list1:
            tmp.next = list1
        else:
            tmp.next = list2

        return head.next


# @lc code=end
