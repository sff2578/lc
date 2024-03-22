#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (41.22%)
# Likes:    15300
# Dislikes: 4140
# Total Accepted:    2.6M
# Total Submissions: 6.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return ret
            curC = strs[0][i]
            for idx, str in enumerate(strs):
                if i >= len(str):
                    return ret
                if str[i] != curC:
                    return ret
            ret += curC
            i += 1

        return ret


# @lc code=end
