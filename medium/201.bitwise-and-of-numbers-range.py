#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (42.58%)
# Likes:    3206
# Dislikes: 227
# Total Accepted:    271.5K
# Total Submissions: 630.2K
# Testcase Example:  '5\n7'
#
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
#
#
# Example 1:
#
#
# Input: left = 5, right = 7
# Output: 4
#
#
# Example 2:
#
#
# Input: left = 0, right = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= left <= right <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # loop through each bit,
        # check all nums of this bit, if there's a 1, mark it
        res = 0
        for i in range(32):
            bit = 1
            for num in range(left, right + 1):
                bit &= num & 1
                if not bit:
                    break
            res += bit << i
            left >>= 1
            right >>= 1
            if not left and not right:
                break
        return res

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # e.g. 5-10, looking for a bit that all numbers are 1
        # 0101
        # 0110
        # 0111
        # 1000
        # 1001
        # 1010
        # last bit will always be 0 1 0 1 for even/odd numbers
        # when shift right, will form a new range with some numbers dupliate, but still continous, so it'll again be 0 1 0 1
        # until there's only 1 number, which will be either 1 or 0
        # if this last number was at n-th bit, then n << 1(or 0)
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i


# @lc code=end
