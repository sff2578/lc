#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (55.12%)
# Likes:    9879
# Dislikes: 1339
# Total Accepted:    1.3M
# Total Submissions: 2.4M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        next = 0
        while True:
            while n > 0:
                res = n % 10
                n = n // 10
                next += res * res
            if next == 1:
                return True
            if next in seen:
                return False
            seen.add(next)
            n, next = next, 0
        return True


# @lc code=end
