#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (51.45%)
# Likes:    5310
# Dislikes: 223
# Total Accepted:    218.3K
# Total Submissions: 425.7K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
# 
# 
# Example 2:
# 
# 
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
# @lc code=end

