#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (44.91%)
# Likes:    3825
# Dislikes: 191
# Total Accepted:    1.3M
# Total Submissions: 2.8M
# Testcase Example:  '"Hello World"'
#
# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
# Example 1:
#
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
#
# Example 2:
#
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
#
# Example 3:
#
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
#
#
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        maxLen, curLen = 0, 0
        for i in range(len(s)):
            if s[i] == " ":
                if curLen != 0:
                    maxLen = curLen
                curLen = 0
            else:
                curLen += 1
        return maxLen


# @lc code=end
