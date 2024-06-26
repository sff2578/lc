#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (70.37%)
# Likes:    8297
# Dislikes: 480
# Total Accepted:    743K
# Total Submissions: 1M
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
#'[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]'
#
# Implement the BSTIterator class that represents an iterator over the in-order
# traversal of a binary search tree (BST):
#
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
# The root of the BST is given as part of the constructor. The pointer should
# be initialized to a non-existent number smaller than any element in the
# BST.
# boolean hasNext() Returns true if there exists a number in the traversal to
# the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the
# pointer.
#
#
# Notice that by initializing the pointer to a non-existent smallest number,
# the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be
# at least a next number in the in-order traversal when next() is called.
#
#
# Example 1:
#
#
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next",
# "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
#  7
# 3   15
#   9 20
#
# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.
#
#
#
# Follow up:
#
#
# Could you implement next() and hasNext() to run in average O(1) time and use
# O(h) memory, where h is the height of the tree?
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
class BSTIterator:
    # smallest number will be left most child,
    # next will be the (left most child of my right child)
    # every time i found next, push in the left tree of my right child(the next smallest one will be at top of stack)
    def __init__(self, root: Optional[TreeNode]):
        self.ary = [-1] + self.inOrderTrav(root)
        self.cur_idx = 0
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def pushAll(self, root):
        if root == None:
            return
        while root != None:
            self.stack.append(root)
            root = root.left

    def inOrderTrav(self, root) -> list:
        if root == None:
            return []
        left = self.inOrderTrav(root.left)
        right = self.inOrderTrav(root.right)
        return left + [root.val] + right


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
