#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (70.88%)
# Likes:    11050
# Dislikes: 214
# Total Accepted:    1.3M
# Total Submissions: 1.8M
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal, each recursive function return the list of it's children
        # return if we found max k children
        self.debug = True
        self.k = k
        if self.debug:
            print("k is ", self.k)
        self.val = 0
        list_a = self.inorder(root)
        if self.debug:
            print("list_a, ", list_a)
        return self.val

        # inorder
        # l = self.inorderTraversal(root)
        # return l[k - 1]

    def inorder(self, root):
        cur_l = []
        if root.left == None and root.right == None:
            cur_l = [root.val]
            if len(cur_l) >= self.k:
                if self.debug:
                    print("after right, found val, ", cur_l, self.k)
                self.val = cur_l[self.k - 1]
                self.k = 0
                return cur_l
            else:
                return cur_l
        else:
            if root.left:
                cur_l += self.inorder(root.left)
            cur_l.append(root.val)
            if self.k == 0:
                if self.debug:
                    print("after left, k is 0, ", cur_l)
                return cur_l
            if len(cur_l) >= self.k:
                self.val = cur_l[self.k - 1]
                self.k = 0
                if self.debug:
                    print("after left, found val, ", cur_l, self.k)
                return cur_l
            if root.right:
                cur_l += self.inorder(root.right)
                if self.k == 0:
                    if self.debug:
                        print("after left, k is 0, ", cur_l)
                    return cur_l
            if self.k == 0:
                if self.debug:
                    print("after left, k is 0, ", cur_l)
                return cur_l
            if len(cur_l) >= self.k:
                if self.debug:
                    print("after right, found val, ", cur_l, self.k)
                self.val = cur_l[self.k - 1]
                self.k = 0
                return cur_l
            else:
                return cur_l

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


# [45,30,46,10,36,null,49,8,24,34,42,48,null,4,9,14,25,31,35,41,43,47,null,0,6,null,null,11,20,null,28,null,33,null,null,37,null,null,44,null,null,null,1,5,7,null,12,19,21,26,29,32,null,null,38,null,null,null,3,null,null,null,null,null,13,18,null,null,22,null,27,null,null,null,null,null,39,2,null,null,null,15,null,null,23,null,null,null,40,null,null,null,16,null,null,null,null,null,17]
#' +
#'32

# @lc code=end
