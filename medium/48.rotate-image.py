#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (72.02%)
# Likes:    16824
# Dislikes: 754
# Total Accepted:    1.5M
# Total Submissions: 2.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
#
#
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap up down, then symmetriy(对角线)
        # 1 2 3     7 8 9       7 4 1
        # 4 5 6 ->  4 5 6 ->    8 5 2
        # 7 8 9     1 2 3       9 6 3
        # swap rows
        n = len(matrix)
        i, j = 0, n - 1
        while i < j:
            for k in range(n):
                tmp = matrix[j][k]
                matrix[j][k] = matrix[i][k]
                matrix[i][k] = tmp
            i += 1
            j -= 1
        # swap diagnal
        for row in range(n):
            for col in range(row + 1, n):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp
        return


# @lc code=end
