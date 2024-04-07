#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (50.67%)
# Likes:    15145
# Dislikes: 815
# Total Accepted:    1.6M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1,2,3
# 1,2,3,4
class Solution:
    # revert the first half, get first half by fast-slow pointers
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        cur = slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            cur.next = prev
            prev, cur = cur, slow
        if fast != None:
            slow = slow.next

        left, right = prev, slow
        while left != None and right != None:
            print(left.val, right.val)
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
        print("first")
        tmp = prev
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next
        print("second")
        tmp = slow
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next


# @lc code=end
