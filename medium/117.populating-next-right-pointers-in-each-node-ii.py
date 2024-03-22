#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (50.79%)
# Likes:    5701
# Dislikes: 311
# Total Accepted:    598.3K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
#
#
#
# Follow-up:
#
#
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
#
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        debug = False
        # level order traversal?
        # the next will point to the same level
        if root == None:
            return root
        q1, q2 = [], []
        q1.append(root)
        prev_node = None
        while q1:
            cur_node = q1.pop(0)
            if prev_node != None:
                prev_node.next = cur_node
            prev_node = cur_node
            if cur_node.left != None:
                q2.append(cur_node.left)
            if cur_node.right != None:
                q2.append(cur_node.right)
            if len(q1) == 0:
                q1 = q2
                q2 = []
                prev_node = None
                if debug:
                    print("q1: ", q1)
                    print("q2: ", q2)
        return root


# [1,2,3,4,5,null,7]


# @lc code=end
