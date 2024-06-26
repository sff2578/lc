#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (54.02%)
# Likes:    5546
# Dislikes: 1062
# Total Accepted:    588.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Given an integer array nums sorted in non-decreasing order, remove some
# duplicates in-place such that each unique element appears at most twice. The
# relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
#
#
# If all assertions pass, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
# Example 2:
#
#
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements
# of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
#
#
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,1,2,2,3]
        # [1,1,1,1,2,2,2,2,3]
        if len(nums) == 0:
            return 0
        cur_v, cur_o = nums[0], 1
        i, j = 1, 1
        while j < len(nums):
            if nums[j] != cur_v:
                nums[i] = nums[j]
                i += 1
                cur_v = nums[j]
                cur_o = 1
            elif nums[j] == cur_v and cur_o < 2:
                cur_o += 1
                nums[i] = nums[j]
                i += 1
            else:
                cur_o += 1
            j += 1

        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        # 03/30/2024
        # save p number and p count
        # j go next every time, if j num not same as p, switch and update p/p count
        #  otherwise p_cnt++
        # change i if j not same with p or p_cnt <2
        p, p_cnt = nums[0], 1
        i, j = 1, 1
        while j < len(nums):
            if nums[j] != p or (nums[j] == p and p_cnt < 2):
                if nums[j] != p:
                    p, p_cnt = nums[j], 1
                else:
                    p_cnt += 1
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


# @lc code=end
