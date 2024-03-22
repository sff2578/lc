#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (40.45%)
# Likes:    14895
# Dislikes: 615
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs backtrack
        # given each cordinate, remaining string, check all 4 direction for next char
        # if not found, return false, if no next char, return true
        # else dfs to next cord + remaining string, combine all 4 results, if 1 true then return true
        # need to keep visited cords, add to visited one start of function, before every return, remove cord from visited
        visited = set()

        def dfs(r, c, word):
            if len(word) == 0:
                return True
            next_c = word[0]
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ret = False
            visited.add((r, c))
            for i, j in dirs:
                nr, nc = r + i, c + j
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                    if (nr, nc) not in visited and board[nr][nc] == next_c:
                        # found a match
                        ret |= dfs(nr, nc, word[1:])
                        if ret:
                            return ret
            if not ret:
                visited.remove((r, c))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c == word[0]:
                    ret = dfs(i, j, word[1:])
                    if ret:
                        return True
        return False


# @lc code=end
