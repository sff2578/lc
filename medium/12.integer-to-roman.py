#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (62.65%)
# Likes:    6112
# Dislikes: 5229
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '3'
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
# For example, 2 is written as II in Roman numeral, just two one's added
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
# Given an integer, convert it to a roman numeral.
#
#
# Example 1:
#
#
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
#
#
# Example 2:
#
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
# Example 3:
#
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#
# 1 <= num <= 3999
#
#
#


# @lc code=start
class Solution:
    # if > 1000, repeat M, if 900, CM, if 500-900 D, if 400 CD, if 100-400 repeat C, if 90 XC, if 50-90 L, if 40XL, if 10-30 repeat X, if 9 IX,
    # if 5-8 V, if 4 IV, if 1-3 repeat I
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    def intToRoman(self, num: int) -> str:
        ret = ""
        if num == 0:
            return ret
        if num >= 1000:
            for i in range(num // 1000):
                ret += "M"
            ret += self.intToRoman(num % 1000)
        elif num >= 900:
            ret += "CM" + self.intToRoman(num - 900)
        elif num >= 500:
            ret += "D" + self.intToRoman(num - 500)
        elif num >= 400:
            ret += "CD" + self.intToRoman(num - 400)
        elif num >= 100:
            for i in range(num // 100):
                ret += "C"
            ret += self.intToRoman(num % 100)
        elif num >= 90:
            ret += "XC" + self.intToRoman(num - 90)
        elif num >= 50:
            ret += "L" + self.intToRoman(num - 50)
        elif num >= 40:
            ret += "XL" + self.intToRoman(num - 40)
        elif num >= 10:
            for i in range(num // 10):
                ret += "X"
            ret += self.intToRoman(num % 10)
        elif num >= 9:
            ret += "IX" + self.intToRoman(num - 9)
        elif num >= 5:
            ret += "V" + self.intToRoman(num - 5)
        elif num >= 4:
            ret += "IV" + self.intToRoman(num - 4)
        elif num >= 1:
            for i in range(num // 1):
                ret += "I"
        return ret


# @lc code=end
