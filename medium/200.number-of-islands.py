#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (57.52%)
# Likes:    21831
# Dislikes: 477
# Total Accepted:    2.5M
# Total Submissions: 4.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind()

        def valid_cord(i, j, grid):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                return True
            return False

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                uf.find((i, j))
                for off_i, off_j in directions:
                    if (
                        valid_cord(i + off_i, j + off_j, grid)
                        and grid[i + off_i][j + off_j] == "1"
                    ):
                        uf.union((i, j), (i + off_i, j + off_j))

        # uf.print()
        islands = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                parent = uf.find((i, j))
                if parent in islands:
                    islands[parent] += 1
                else:
                    islands[parent] = 1
        return len(islands)


class UnionFind:
    def __init__(self):
        self.parent = dict()

    def print(self):
        from pprint import pprint

        pprint(self.parent)

    def find(self, cord):
        if cord in self.parent:
            if self.parent[cord] != cord:
                self.parent[cord] = self.find(self.parent[cord])
        else:
            self.parent[cord] = cord
        return self.parent[cord]

    def union(self, cord1, cord2):
        # print("unioning ", cord1, cord2)
        p_cord1 = self.find(cord1)
        p_cord2 = self.find(cord2)
        self.parent[p_cord2] = p_cord1
        return


# @lc code=end
