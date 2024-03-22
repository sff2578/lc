#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (43.70%)
# Likes:    5952
# Dislikes: 473
# Total Accepted:    386K
# Total Submissions: 838.7K
# Testcase Example:  '"abab"'
#
# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
#
#
# Example 1:
#
#
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#
#
# Example 2:
#
#
# Input: s = "aba"
# Output: false
#
#
# Example 3:
#
#
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc"
# twice.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    # abcabcd -> bcabc,abcab
    # ababa
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            found = True
            for start in range(0, len(s), i):
                if start + i > len(s):
                    found = False
                elif s[0:i] != s[start : start + i]:
                    found = False
            if found:
                return True
        return False


# @lc code=end
