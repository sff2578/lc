#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (58.95%)
# Likes:    11801
# Dislikes: 677
# Total Accepted:    2.9M
# Total Submissions: 4.9M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
#
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
#
# Example 2:
#
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 3:
#
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
#
#

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        print(rToInt)
        res = 0
        for i in range(len(s)):
            if s[i] == "I":
                if i + 1 < len(s):
                    if s[i + 1] == "V":
                        res += 4
                        i += 1
                    elif s[i + 1] == "X":
                        res += 9
                        i += 1
                    else:
                        res += 1
                else:
                    res += 1
            elif s[i] == "X":
                if i + 1 < len(s):
                    if s[i + 1] == "L":
                        res += 40
                        i += 1
                    elif s[i + 1] == "C":
                        res += 90
                        i += 1
                    else:
                        res += 10
                else:
                    res += 10
            elif s[i] == "C":
                if i + 1 < len(s):
                    if s[i + 1] == "D":
                        res += 400
                        i += 1
                    elif s[i + 1] == "M":
                        res += 900
                        i += 1
                    else:
                        res += 100
                else:
                    res += 100
            else:
                res += rToInt[s[i]]
        return res


# @lc code=end
