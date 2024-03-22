#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Medium (42.54%)
# Likes:    3108
# Dislikes: 1941
# Total Accepted:    432.7K
# Total Submissions: 1M
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
#
# Example 2:
#
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
#
# Example 3:
#
#
# Input: n = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^4
#
#
#
# Follow up: Could you write a solution that works in logarithmic time
# complexity?
#
#


# @lc code=start
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_two, num_five = 0, 0
        for i in range(n + 1):
            twos, fives = i, i
            while twos > 0:
                if twos % 2 == 0:
                    num_two += 1
                    twos = twos // 2
                else:
                    break
            while fives > 0:
                if fives % 5 == 0:
                    num_five += 1
                    fives = fives // 5
                else:
                    break
        return min(num_five, num_two)

    def trailingZeroes(self, n: int) -> int:
        # count number of 5, use the last number (n)//5 is the number of 5
        cnt = 0
        while n > 0:
            cnt += n // 5
            n //= 5
        return cnt


# @lc code=end
