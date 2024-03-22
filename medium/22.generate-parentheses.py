#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.09%)
# Likes:    20392
# Dislikes: 868
# Total Accepted:    1.7M
# Total Submissions: 2.3M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs, start with 0 left 0 right, always can place left when l < n, only can place right when l > n
        # if l == n, can only place right
        def dfs(l, r):
            if l == n:
                # can only place right
                rem = ")" * (n - r)
                return [rem]
            ret = []
            if l > r:
                # can place right
                r_ret = dfs(l, r + 1)
                for item in r_ret:
                    item = ")" + item
                    ret.append(item)
            # always can place left
            l_ret = dfs(l + 1, r)
            for item in l_ret:
                item = "(" + item
                ret.append(item)
            return ret

        return dfs(0, 0)


# @lc code=end
