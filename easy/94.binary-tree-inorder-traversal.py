#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (74.43%)
# Likes:    13061
# Dislikes: 732
# Total Accepted:    2.4M
# Total Submissions: 3.1M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur_l = []
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        cur_l += self.inorderTraversal(root.left)
        cur_l.append(root.val)
        cur_l += self.inorderTraversal(root.right)
        return cur_l


# @lc code=end
