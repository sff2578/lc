#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.42%)
# Likes:    7658
# Dislikes: 389
# Total Accepted:    628.3K
# Total Submissions: 1.6M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
#
#
# Example 1:
#
#
# Input: s = "aba"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # valid sub string
        i, j = 0, len(s) - 1
        while j > i:
            if s[i] != s[j]:
                return self.validSubStr(s, i, j - 1) or self.validSubStr(s, i + 1, j)
            j -= 1
            i += 1
        return True

    def validSubStr(self, s, start, end):
        # aba,abba
        while end > start:
            if s[end] != s[start]:
                return False
            end -= 1
            start += 1
        return True


# @lc code=end
