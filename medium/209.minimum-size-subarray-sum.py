#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (46.37%)
# Likes:    11993
# Dislikes: 373
# Total Accepted:    906.7K
# Total Submissions: 1.9M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to
# target. If there is no such subarray, return 0 instead.
#
#
# Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
# Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
# Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window, start, end keeps going until >= target, then start++ until < target, end++ again
        back, forward, res, sum = 0, 0, len(nums), nums[0]
        found = False
        while back < len(nums) and forward < len(nums):
            if sum >= target:
                found = True
                if back == forward:
                    return 1
                res = min(res, forward - back + 1)
                sum -= nums[back]
                back += 1
            else:
                forward += 1
                if forward >= len(nums):
                    break
                sum += nums[forward]
        if found:
            return res
        else:
            return 0


# @lc code=end
