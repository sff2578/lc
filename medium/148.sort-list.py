#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (55.92%)
# Likes:    11162
# Dislikes: 330
# Total Accepted:    735.2K
# Total Submissions: 1.3M
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
#
#
# Example 1:
#
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
#
# Example 2:
#
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        # given the start, middle, end node of an array
        # divide to 2 array, recursive on each of them
        # after come back, merge
        def dfs(head, end):
            # head included, end not included
            # print(hex(id(head)), hex(id(end)))
            if head == end or head.next == end:
                if head != None:
                    head.next = None
                return head
            slow, fast = head, head
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            # print("left start")
            left_h = dfs(head, slow)
            # print("left end")
            # print("right start")
            right_h = dfs(slow, end)
            # print("right end")
            new_h = ListNode()
            tmp = new_h
            while left_h is not None and right_h is not None:
                if left_h.val <= right_h.val:
                    tmp.next = left_h
                    left_h = left_h.next
                else:
                    tmp.next = right_h
                    right_h = right_h.next
                tmp = tmp.next
            while left_h is not None:
                tmp.next = left_h
                tmp = tmp.next
                left_h = left_h.next
            while right_h is not None:
                tmp.next = right_h
                tmp = tmp.next
                right_h = right_h.next
            tmp.next = None
            return new_h.next

        return dfs(head, None)


# @lc code=end
