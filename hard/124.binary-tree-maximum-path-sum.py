#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (39.39%)
# Likes:    16069
# Dislikes: 701
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty
# path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#  -10
# 9   20
#   15 7
# recursive for each node:
# each node return 2: max include this node and max not include this node
# 1. use this node: left_max(if not neg) + this node + right_max(if not neg)
# 2. not use this node: max(left, right)
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #  -10(41, 42)
        # 9(9,0)   20 (42, 15)
        #   15 7
        #   15,0 7,0
        # recursive for each node:
        # each node return 2: max include this node and max not include this node
        # 1. use this node: left_max(if not neg) + this node + right_max(if not neg)
        # 2. not use this node: max(left, right)
        if root.left == None and root.right == None:
            return root.val
        res = self.maxPathSumHelper(root)
        return max(res[0], res[1])

    def maxPathSumHelper(self, root) -> []:
        hasPositive, maxNeg = False, -1001
        if root == None:
            return [0, -1001]
        left_max = self.maxPathSumHelper(root.left)
        right_max = self.maxPathSumHelper(root.right)

        # user current root and connect to parent
        use_node = root.val
        if max(left_max[0], right_max[0]) >= 0:
            use_node += max(left_max[0], right_max[0])
        # max path is in left or right, or left+cur+right
        a = root.val
        if left_max[0] >= 0:
            a += left_max[0]
        if right_max[0] >= 0:
            a += right_max[0]
        not_use = max(left_max[1], right_max[1], a)
        return [use_node, not_use]


# [5,4,8,11,null,13,4,7,2,null,null,null,1]


# @lc code=end
