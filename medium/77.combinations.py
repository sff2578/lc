#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (68.07%)
# Likes:    8001
# Dislikes: 209
# Total Accepted:    847.4K
# Total Submissions: 1.2M
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        if k == 1:
            for i in range(1, n + 1):
                ret.append([i])
            return ret
        dfs_ret = self.combine(n, k - 1)
        for entry in dfs_ret:
            last_n = entry[-1]
            for i in range(last_n + 1, n + 1):
                new_ent = entry + [i]
                ret.append(new_ent)
        return ret


# @lc code=end
