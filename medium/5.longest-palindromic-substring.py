#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (33.68%)
# Likes:    28725
# Dislikes: 1718
# Total Accepted:    2.9M
# Total Submissions: 8.8M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2d dp, p(i,j) = (vi==vj and p[i+1, j-1])
        # base: 00, 11, 22 etc true,
        #   check 01, 12, 23 etc
        maxL = 1
        ret = s[0]
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if maxL < 2:
                    maxL = 2
                    ret = s[i : i + 2]
        # print(dp)
        for j in range(2, len(s)):
            for i in range(j - 1):
                # print(j, i, dp[i + 1][j - 1])
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if maxL < (j - i + 1):
                        maxL = j - i + 1
                        ret = s[i : j + 1]
        return ret


# @lc code=end
