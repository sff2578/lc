#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (35.76%)
# Likes:    10746
# Dislikes: 1289
# Total Accepted:    851.4K
# Total Submissions: 2.4M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort, add tuple to set to make sure unique
        nums.sort()
        res = set()
        if len(nums) < 4:
            return res
        for i in range(0, len(nums) - 3):
            three_sum_res = self.threeSum(nums, i + 1, target - nums[i])
            for val1, val2, val3 in three_sum_res:
                res.add((nums[i], val1, val2, val3))
        return res

    def threeSum(self, nums, start, target) -> List[List[int]]:
        # loop + 2 sum
        # print(nums)
        res = set()
        for i in range(start, len(nums) - 2):
            two_sum_res = self.twoSum(nums, i + 1, target - nums[i])
            for val1, val2 in two_sum_res:
                res.add((nums[i], val1, val2))
        return res

    def twoSum(self, nums, start, target):
        # print(start, target)
        rec = dict()
        res = set()
        for i in range(start, len(nums)):
            if nums[i] in rec.keys():
                res.add((nums[rec[nums[i]]], nums[i]))
            else:
                rec[target - nums[i]] = i
        # print(res)
        return res


# @lc code=end

# The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum. Some optimization was be made knowing the list is sorted.
