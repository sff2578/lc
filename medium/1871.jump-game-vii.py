#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#
# https://leetcode.com/problems/jump-game-vii/description/
#
# algorithms
# Medium (24.90%)
# Likes:    1481
# Dislikes: 83
# Total Accepted:    37.2K
# Total Submissions: 149.6K
# Testcase Example:  '"011010"\n2\n3'
#
# You are given a 0-indexed binary string s and two integers minJump and
# maxJump. In the beginning, you are standing at index 0, which is equal to
# '0'. You can move from index i to index j if the following conditions are
# fulfilled:
#
#
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
#
#
# Return true if you can reach index s.length - 1 in s, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3.
# In the second step, move from index 3 to index 5.
#
#
# Example 2:
#
#
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
#
#
#
# Constraints:
#
#
# 2 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
#
#
#


# @lc code=start
class Solution:
    # 01101110 2,3
    # i: can we reach i? meaning between [i-maxJ, i-minJ], any reachable 0?
    #   use sliding window to check if any reachable 0
    #   if i-maxJ-1 is reachable 0, count-1, if i-minJ is count+1
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        pre = 1
        res = [False] * len(s)
        res[0] = True
        for i in range(1, len(s)):
            if i - minJump >= 0 and res[i - minJump]:
                pre += 1
            if i - maxJump >= 0 and res[i - maxJump - 1]:
                pre -= 1
            res[i] = s[i] == "0" and pre > 1
        return res[len(s) - 1]


# @lc code=end
