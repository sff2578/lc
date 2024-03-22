#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (37.55%)
# Likes:    8277
# Dislikes: 1731
# Total Accepted:    644.2K
# Total Submissions: 1.7M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
#
# Example 1:
#
#
# Input: board =
# [["X","X","X","X"],
# .["X","O","O","X"],
#  ["X","X","O","X"],
# .["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#
#


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # union find, make the parent the one on boarder(if there's one)
        # at the end, go through board again, if parent is not on boarder, flip
        def cordValid(i, j, board):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            return True

        uf = UnionFind(board)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    continue
                for off_i, off_j in directions:
                    uf.find((i, j))  # update this parent
                    if (
                        cordValid(i + off_i, j + off_j, board)
                        and board[i + off_i][j + off_j] == "O"
                    ):
                        uf.union((i, j), (i + off_i, j + off_j))

        # loop again to flap
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    continue
                if not uf.isBoarder(uf.find((i, j))):
                    board[i][j] = "X"
        return


class UnionFind:
    def __init__(self, board):
        self.parents = dict()
        self.rows = len(board)
        self.cols = len(board[0])

    def find(self, cord):
        if cord in self.parents:
            if self.parents[cord] != cord:
                self.parents[cord] = self.find(self.parents[cord])
        else:
            self.parents[cord] = cord
        return self.parents[cord]

    def union(self, cord1, cord2):
        p_cord1 = self.find(cord1)
        p_cord2 = self.find(cord2)
        if self.isBoarder(p_cord1):
            self.parents[p_cord2] = p_cord1
        else:
            self.parents[p_cord1] = p_cord2

    def isBoarder(self, cord):
        if (
            cord[0] == 0
            or cord[0] == self.rows - 1
            or cord[1] == 0
            or cord[1] == self.cols - 1
        ):
            return True
        return False


# @lc code=end
