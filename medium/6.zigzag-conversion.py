#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (45.48%)
# Likes:    6581
# Dislikes: 13014
# Total Accepted:    1.1M
# Total Submissions: 2.4M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#


# @lc code=start
class Solution:
    # calculate
    # AB 1
    def convert(self, s: str, numRows: int) -> str:
        ret = ""
        if numRows == 1 or len(s) == numRows:
            return s
        for i in range(numRows):
            prev = j = i
            ret += s[j]
            print("i:", i)
            while j < len(s):
                j = prev + (numRows - i - 1) * 2
                print("j:", j)
                if j >= len(s):
                    break
                if j != prev:
                    ret += s[j]
                    prev = j
                j = prev + i * 2
                print("j2:", j)
                if j >= len(s):
                    break
                if j != prev:
                    ret += s[j]
                    prev = j
        return ret


# @lc code=end
