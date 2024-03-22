#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (50.50%)
# Likes:    18930
# Dislikes: 687
# Total Accepted:    1.9M
# Total Submissions: 3.6M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#
# Constraints:
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap
        # NOTICE: when using tuple as heap element, if first ele of tuple same, will continue to compare 2 ele of tuple, so need to put i to avoid ListNode compare
        if len(lists) == 0:
            return None
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        head = ListNode()
        cur = head
        while len(heap) > 0:
            _, i, cur.next = heappop(heap)
            cur = cur.next
            if cur.next:
                heappush(heap, (cur.next.val, i, cur.next))
        return head.next

    def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        l1 = lists.pop(0)
        l2 = lists.pop(0)

        def merge(l1, l2):
            head = ListNode(0)
            tmp = head
            while l1 != None or l2 != None:
                if l1 is None:
                    tmp.next = l2
                    break
                elif l2 is None:
                    tmp.next = l1
                    break
                elif l1.val < l2.val:
                    tmp.next = l1
                    l1 = l1.next
                else:
                    tmp.next = l2
                    l2 = l2.next
                tmp = tmp.next
            return head.next

        h = merge(l1, l2)
        lists.append(h)
        return self.mergeKLists(lists)


# @lc code=end
