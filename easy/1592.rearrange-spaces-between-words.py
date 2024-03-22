#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#
# https://leetcode.com/problems/rearrange-spaces-between-words/description/
#
# algorithms
# Easy (43.32%)
# Likes:    407
# Dislikes: 327
# Total Accepted:    50.4K
# Total Submissions: 116.1K
# Testcase Example:  '"  this   is  a sentence "'
#
# You are given a string text of words that are placed among some number of
# spaces. Each word consists of one or more lowercase English letters and are
# separated by at least one space. It's guaranteed that text contains at least
# one word.
#
# Rearrange the spaces so that there is an equal number of spaces between every
# pair of adjacent words and that number is maximized. If you cannot
# redistribute all the spaces equally, place the extra spaces at the end,
# meaning the returned string should be the same length as text.
#
# Return the string after rearranging the spaces.
#
#
# Example 1:
#
#
# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. We can evenly divide
# the 9 spaces between the words: 9 / (4-1) = 3 spaces.
#
#
# Example 2:
#
#
# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces
# plus 1 extra space. We place this extra space at the end of the string.
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 100
# text consists of lowercase English letters and ' '.
# text contains at least one word.
#
#
#


# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        wordL = 0
        for word in words:
            wordL += len(word)
        nSpaces = len(text) - wordL
        if len(words) == 1:
            return words[0] + " " * nSpaces
        innerS = nSpaces // (len(words) - 1)
        endS = nSpaces % (len(words) - 1)
        ret = ""
        for i in range(len(words) - 1):
            ret += words[i] + " " * innerS
        return ret + words[-1] + " " * endS


# @lc code=end
