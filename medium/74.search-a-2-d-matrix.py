#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (48.28%)
# Likes:    15197
# Dislikes: 402
# Total Accepted:    1.6M
# Total Submissions: 3.3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# You are given an m x n integer matrix matrix with the following two
# properties:
#
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Given an integer target, return true if target is in matrix or false
# otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search, serialize, matrix of n row m col, matrix(i,j) = i*m+j
        # eg. matrix of 5 row and 6 col, index (4, 5), last element is 4*6+5 = 29
        # reversely, i = 29//m=29//6=4, j = 29%m = 29%6=5
        # 5: 5//6 = 0 5%6 = 5 (0,5) 6: 6//6 = 1, 6%6 = 0 (1, 0)
        n = len(matrix)
        m = len(matrix[0])
        end = m * n - 1

        def recursive(start, end):
            if start > end:
                return False
            mid = (start + end) // 2
            s_i, s_j = start // m, start % m
            e_i, e_j = end // m, end % m
            m_i, m_j = mid // m, mid % m
            if target in {matrix[s_i][s_j], matrix[e_i][e_j], matrix[m_i][m_j]}:
                return True
            if target < matrix[m_i][m_j]:
                return recursive(start, mid - 1)
            else:
                return recursive(mid + 1, end)

        return recursive(0, end)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 03/36/2024
        # serialize and iterative
        row, col = len(matrix), len(matrix[0])
        s, e = 0, row * col - 1
        while s <= e:
            mid = (s + e) // 2
            c = mid % col
            r = mid // col
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                # left
                e = mid - 1
            else:
                # right
                s = mid + 1
        return False


# @lc code=end
