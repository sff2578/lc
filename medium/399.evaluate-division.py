#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (61.37%)
# Likes:    8950
# Dislikes: 852
# Total Accepted:    435K
# Total Submissions: 707.4K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
#'[2.0,3.0]\n' +
#  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# j^th query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
#
# Note: The variables that do not occur in the list of equations are undefined,
# so the answer cannot be determined for them.
#
#
# Example 1:
#
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
#
# Example 2:
#
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#
#
# Example 3:
#
#
# Input: equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
#
# Constraints:
#
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
#
#
#


# @lc code=start
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1 / v

        def dfs(start, end, visited):
            if start == end:
                return 1
            visited.add(start)
            for k, v in graph[start].items():
                if k not in visited:
                    ret = dfs(k, end, visited)
                    if ret != -1:
                        return ret * v
            visited.discard(start)
            return -1

        # print(graph)
        ret = []
        for start, end in queries:
            if start not in graph or end not in graph:
                ret.append(-1)
            else:
                visited = set()
                ret.append(dfs(start, end, visited))
        return ret


# @lc code=end
