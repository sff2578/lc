#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (52.93%)
# Likes:    20404
# Dislikes: 416
# Total Accepted:    1.6M
# Total Submissions: 2.9M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = so far the longest one = max(dp[0]..dp[i-1]) +1
        # init with 1
        dp = [0] * len(nums)
        dp[0] = 1
        res = 1
        for idx in range(1, len(nums)):
            num = nums[idx]
            for i in range(idx):
                if num > nums[i]:
                    dp[idx] = max(dp[idx], dp[i])
            dp[idx] += 1
            res = max(res, dp[idx])
            # print("number ", num, "dp", dp[idx])
        return res


# @lc code=end
