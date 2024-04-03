#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.56%)
# Likes:    7904
# Dislikes: 4457
# Total Accepted:    1.9M
# Total Submissions: 4.8M
# Testcase Example:  '4'
#
# Given a non-negative integer x, return the square root of x rounded down to
# the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down
# to the nearest integer, 2 is returned.
#
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 03/29/2024
        # 1 - x Binary search
        # instead of finding the last number k that k*k < x
        # try to find the first number k that k*k >= x
        # this way we can do e=mid-1 and no need to check s+1<e
        s, e = 1, x
        if x <= 1:
            return x

        while s < e:
            mid = s + (e - s) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                e = mid
            else:
                s = mid + 1

        return s - 1


# @lc code=end
