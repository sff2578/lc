#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (52.54%)
# Likes:    9151
# Dislikes: 936
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_l, b_l = list(a), list(b)
        res = []
        carry = 0
        while a_l or b_l or carry:
            if a_l:
                carry += int(a_l.pop())
            if b_l:
                carry += int(b_l.pop())
            res.append(str(carry % 2))
            carry = carry // 2
        return "".join(res[::-1])

    def addBinary_1(self, a: str, b: str) -> str:
        # 1011
        # 100
        ac, bc = len(a) - 1, len(b) - 1
        carry, res = 0, ""
        while ac >= 0 and bc >= 0:
            if a[ac] == "1" and b[bc] == "1":
                if carry == 1:
                    res = "1" + res
                else:
                    res = "0" + res
                carry = 1
            elif a[ac] == "0" and b[bc] == "0":
                # chec carry, will not update carry
                if carry == 1:
                    res = "1" + res
                else:
                    res = "0" + res
                carry = 0
            else:
                # one is 1, if carry is 1 then result 0 carry 1, else result 1 and no carry
                if carry == 1:
                    res = "0" + res
                else:
                    res = "1" + res
            ac -= 1
            bc -= 1
        while ac >= 0:
            if a[ac] == "0":
                if carry == 1:
                    res = "1" + res
                    carry = 0
                else:
                    res = "0" + res
            else:
                if carry == 1:
                    res = "0" + res
                else:
                    res = "1" + res
            ac -= 1
        while bc >= 0:
            if b[bc] == "0":
                if carry == 1:
                    res = "1" + res
                    carry = 0
                else:
                    res = "0" + res
            else:
                if carry == 1:
                    res = "0" + res
                else:
                    res = "1" + res
            bc -= 1
        if carry == 1:
            res = "1" + res
        return res


# @lc code=end
