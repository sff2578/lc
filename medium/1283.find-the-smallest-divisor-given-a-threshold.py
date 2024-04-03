#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
#
# algorithms
# Medium (59.15%)
# Likes:    2785
# Dislikes: 193
# Total Accepted:    164.9K
# Total Submissions: 278.1K
# Testcase Example:  '[1,2,5,9]\n6'
#
# Given an array of integers nums and an integer threshold, we will choose a
# positive integer divisor, divide all the array by it, and sum the division's
# result. Find the smallest divisor such that the result mentioned above is
# less than or equal to threshold.
#
# Each result of the division is rounded to the nearest integer greater than or
# equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
#
# The test cases are generated so that there will be an answer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5
# the sum will be 5 (1+1+1+2).
#
#
# Example 2:
#
#
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6
#
#
#

from math import ceil


# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 03/29/2024
        # same as 875, min is 1, max is the max of array, binary search
        max_num = nums[0]
        for num in nums:
            max_num = max(max_num, num)

        def divison_sum(mid):
            res = 0
            for num in nums:
                res += ceil(num / mid)
            return res

        s, e = 1, max_num

        while s < e:
            mid = s + (e - s) // 2
            if divison_sum(mid) > threshold:
                s = mid + 1
            else:
                e = mid

        return s


# @lc code=end
