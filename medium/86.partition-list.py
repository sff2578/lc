#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (52.64%)
# Likes:    7122
# Dislikes: 817
# Total Accepted:    580.7K
# Total Submissions: 1M
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # go over each node, 2 heads:1 for small 1 for big
        # if small, link small_cur to this node, else link big_cur
        # link 2 lists
        first_head, second_head = ListNode(0), ListNode(0)
        cur, small_cur, big_cur = head, first_head, second_head
        while cur != None:
            if cur.val < x:
                small_cur.next = cur
                small_cur = small_cur.next
            else:
                big_cur.next = cur
                big_cur = big_cur.next
            cur = cur.next
        big_cur.next = None
        if second_head.next != None:
            small_cur.next = second_head.next
        return first_head.next


# @lc code=end
