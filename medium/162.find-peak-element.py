#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (45.84%)
# Likes:    11360
# Dislikes: 4580
# Total Accepted:    1.3M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of the
# peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the
# array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
#
#
#


# [1,2,3,1]
# 0,1,2,3
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # find mid: 1. mid is peak, 2. mid is after peak, 3. mid is before peak
        def recursive(s, e):
            if s == e:
                return s
            if s + 1 == e:
                return s if nums[s] > nums[e] else e

            mid = (s + e) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                return recursive(s, mid - 1)
            elif nums[mid + 1] > nums[mid]:
                return recursive(mid + 1, e)
            return -1

        return recursive(0, len(nums) - 1)

        return


# @lc code=end
