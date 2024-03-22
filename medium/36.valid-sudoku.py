#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (58.47%)
# Likes:    10053
# Dislikes: 1042
# Total Accepted:    1.3M
# Total Submissions: 2.2M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.isBlockValid(board, 0, 0, 9):
            return False
        for row_s in range(0, 9, 3):
            for col_s in range(0, 9, 3):
                my_set = set()
                for row in range(row_s, row_s + 3):
                    for col in range(col_s, col_s + 3):
                        num = board[row][col]
                        if num == ".":
                            continue
                        if num in my_set:
                            return False
                        else:
                            my_set.add(num)
        return True

    def isBlockValid(self, board, row_s, col_s, size):
        # check each row
        for row in range(row_s, row_s + size):
            my_set = set()
            for col in range(col_s, col_s + size):
                num = board[row][col]
                if num == ".":
                    continue
                if num in my_set:
                    return False
                else:
                    my_set.add(num)
        # check each col
        for col in range(col_s, col_s + size):
            my_set = set()
            for i in range(row_s, row_s + size):
                num = board[i][col]
                if num == ".":
                    continue
                if num in my_set:
                    return False
                else:
                    my_set.add(num)
        return True


# failed2:
# [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]


# @lc code=end
