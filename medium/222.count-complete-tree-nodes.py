#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (61.62%)
# Likes:    8356
# Dislikes: 475
# Total Accepted:    657.1K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = []
# Output: 0
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if len(root.right) + 1 = len(root): left is complete, recursive calculate root.right, left child is same height of right child
        # else: root.right is complete, recursive calculate root.left
        # number in complete tree
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        root_h, right_h = self.height(root), self.height(root.right)
        count = 1
        for i in range(right_h):
            count += 1 << i
        if right_h + 1 == root_h:
            # if len(root.right) + 1 = len(root): left is complete, recursive calculate root.right, left child is same height of right child
            count += self.countNodes(root.right)
        else:
            count += self.countNodes(root.left)
        return count

    def height(self, root):
        h = 0
        while root != None:
            h += 1
            root = root.left
        return h


# @lc code=end
