#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (40.12%)
# Likes:    6931
# Dislikes: 3274
# Total Accepted:    776.6K
# Total Submissions: 1.9M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
#
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
#
#
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 04/01/2024
        # final array initiated at beginning
        # sum while calculation
        res_ary = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum = res_ary[i + j + 1] + mul
                res_ary[i + j + 1] = sum % 10
                res_ary[i + j] += sum // 10
        ret = ""
        for i, num in enumerate(res_ary):
            if num != 0:
                ret = "".join(str(x) for x in res_ary[i:])
                return ret
        return "0"


# @lc code=end
