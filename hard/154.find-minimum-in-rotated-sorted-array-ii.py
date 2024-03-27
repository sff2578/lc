#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (43.61%)
# Likes:    4603
# Dislikes: 478
# Total Accepted:    439.7K
# Total Submissions: 1M
# Testcase Example:  '[1,3,5]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.
#
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
#
#
#
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates. Would this affect the runtime complexity?
# How and why?
#
#
#
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # same as 153, if vmid > end: s = mid+1
        # if vmid<end: left side, maybe self
        # different is when array rotated at duplicate number:
        # 3323 or 32333, at this point, vstart=vend=vmid, min
        # can be at left or right half, move both s and e 1 step
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (s + e) // 2
            num = nums[mid]
            if num == nums[s] and num == nums[e]:
                e -= 1
            elif num > nums[e]:
                s = mid + 1
            elif num <= nums[e]:
                e = mid
        return nums[s]


# @lc code=end
