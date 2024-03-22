#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (72.23%)
# Likes:    3736
# Dislikes: 255
# Total Accepted:    358.3K
# Total Submissions: 489.1K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#


# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        # to place n queen, each row must place 1, queen col on each row should not overlap, diagnal also should not overlap
        # go through each row and see if a queen can be placed in this row, if no, then no match, otherwise goto next row
        # dfs on row
        # this may not need dfs?
        # keep a set to save all currently used col, and diags
        # trick on diag: same diff(row, col) means a diag line "\", sum(row, col) means a diag line "/"
        col_set, d1_set, d2_set = set(), set(), set()

        def dfs(row, k):
            count = 0
            if row >= n:
                return count
            for c in range(n):
                if c in col_set or row - c in d1_set or row + c in d2_set:
                    continue
                # place queen in c
                if k == 1:
                    # last one, find a match
                    count += 1
                else:
                    col_set.add(c)
                    d1_set.add(row - c)
                    d2_set.add(row + c)
                    count += dfs(row + 1, k - 1)
                    col_set.remove(c)
                    d1_set.remove(row - c)
                    d2_set.remove(row + c)
            return count

        return dfs(0, n)

    def totalNQueens_1(self, n: int) -> int:
        # bfs, if a cube is used, it can not be used in any other combination
        # init a board with 0, 1 as a queen, -1 as blocked
        # duplicate the borad each time, so that we can revert after return from dfs, but may take too much memory
        # will see if able to imporve further
        # duplicate wont work, need to remain the 1's, each loop save the cordinates of the cells that should revert after dfs is back
        board = [[0 for i in range(n)] for j in range(n)]
        count = 0

        def block(i, j):
            blocked = []
            r, c = len(board), len(board[0])
            # block column
            for cur in range(0, r):
                if board[cur][j] == 0:
                    board[cur][j] = -1
                    blocked.append((cur, j))
            # block row
            for cur in range(0, c):
                if board[i][cur] == 0:
                    board[i][cur] = -1
                    blocked.append((i, cur))
            # block left diagnol
            cur_i, cur_j = i - 1, j - 1
            while cur_i >= 0 and cur_i < r and cur_j >= 0 and cur_j < c:
                if board[cur_i][cur_j] == 0:
                    board[cur_i][cur_j] = -1
                    blocked.append((cur_i, cur_j))
                cur_i, cur_j = cur_i - 1, cur_j - 1
            cur_i, cur_j = i + 1, j + 1
            while cur_i >= 0 and cur_i < r and cur_j >= 0 and cur_j < c:
                if board[cur_i][cur_j] == 0:
                    board[cur_i][cur_j] = -1
                    blocked.append((cur_i, cur_j))
                cur_i, cur_j = cur_i + 1, cur_j + 1
            # block right diagnol
            cur_i, cur_j = i - 1, j + 1
            while cur_i >= 0 and cur_i < r and cur_j >= 0 and cur_j < c:
                if board[cur_i][cur_j] == 0:
                    board[cur_i][cur_j] = -1
                    blocked.append((cur_i, cur_j))
                cur_i, cur_j = cur_i - 1, cur_j + 1
            cur_i, cur_j = i + 1, j - 1
            while cur_i >= 0 and cur_i < r and cur_j >= 0 and cur_j < c:
                if board[cur_i][cur_j] == 0:
                    board[cur_i][cur_j] = -1
                    blocked.append((cur_i, cur_j))
                cur_i, cur_j = cur_i + 1, cur_j - 1
            return blocked

        def dfs(k, starti, startj):
            nonlocal count
            ret = False
            for i in range(starti, n):
                for j in range(startj, n):
                    val = board[i][j]
                    if val != 0:
                        continue
                    board[i][j] = 1
                    if k == 1:
                        # last one, add 1 to the cell
                        # increase count
                        # print(board)
                        count += 1
                    else:
                        # going to use this cell(i,j), mark this 1 and block -1
                        blocked = block(i, j)
                        nexti, nextj = 0, 0
                        dfs(k - 1, i + 1, 0)
                        # after done, remove the blocked
                        for r, c in blocked:
                            board[r][c] = 0
                    board[i][j] = 0
            return

        dfs(n, 0, 0)
        return count


# @lc code=end
