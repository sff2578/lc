#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (39.98%)
# Likes:    4493
# Dislikes: 233
# Total Accepted:    1.9M
# Total Submissions: 4.8M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#


# @lc code=start
class Solution:
    # heloello, ell
    # aa, aaa
    # "mississippi" "issip"
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        cur = 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    res = -1
                    break
                if res == -1:
                    res = i
            return res
        return res


# @lc code=end
