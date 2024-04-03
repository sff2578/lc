#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (61.80%)
# Likes:    17676
# Dislikes: 618
# Total Accepted:    1.9M
# Total Submissions: 3M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
# Example 1:
#
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
#
# Example 2:
#
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
#
#


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 03/29/2024
        # dutch flag partition, partition array into 3 sections, 0, 1 and 2
        # i, j points to boundary of 0 and 2(the one that needs to be swapped to 0 or 2)
        # k is middle unsorted part, from 0 to until meet j
        # each time increate i j after swap
        i, j, k = 0, len(nums) - 1, 0
        while k <= j:
            if nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            elif nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            else:
                k += 1


# @lc code=end
