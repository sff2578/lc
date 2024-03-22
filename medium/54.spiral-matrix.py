#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (46.97%)
# Likes:    14062
# Dislikes: 1229
# Total Accepted:    1.3M
# Total Submissions: 2.7M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#


# @lc code=start
class Solution:
    # keep direction sequence: right->up->left->down----right(again)
    # keep visited matrix
    # with current direction, go until bondary or visited, then continue to next direction
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        visited = [[False for j in range(col)] for i in range(row)]
        ret = []
        dir_map = dict()
        dir_map["right"] = "up"
        dir_map["up"] = "left"
        dir_map["left"] = "down"
        dir_map["down"] = "right"
        i, j, cur_d = 0, 0, "right"

        def not_valid(i, j, row, col, visited):
            if i < 0 or i >= row or j < 0 or j >= col or visited[i][j]:
                return True
            return False

        while True:
            if len(ret) == row * col:
                return ret
            if not visited[i][j]:
                ret.append(matrix[i][j])
                visited[i][j] = True
            if cur_d == "right":
                j += 1
                if not_valid(i, j, row, col, visited):
                    j -= 1
                    cur_d = dir_map[cur_d]
            elif cur_d == "up":
                i += 1
                if not_valid(i, j, row, col, visited):
                    i -= 1
                    cur_d = dir_map[cur_d]
            elif cur_d == "left":
                j -= 1
                if not_valid(i, j, row, col, visited):
                    j += 1
                    cur_d = dir_map[cur_d]
            elif cur_d == "down":
                i -= 1
                if not_valid(i, j, row, col, visited):
                    i += 1
                    cur_d = dir_map[cur_d]


# @lc code=end
