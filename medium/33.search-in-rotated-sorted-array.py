#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (39.29%)
# Likes:    25381
# Dislikes: 1507
# Total Accepted:    2.5M
# Total Submissions: 6.3M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
#
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
#
#
#


# @lc code=start
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target: int) -> int:
        # find min num index
        # use (s = min_idx, e = last_idx+min_idx) as ascending array and do binary search
        # each mid = (s+e)//2, need convert to real index = mid%len(nums)
        # trick to make BS easier, as (s+e)//2 always point to either middle or front one, e.g only 2 number [1,2], mid will be front one "1", so if pick right sub, use mid+1,e if pick left sub, use s+mid, in this case, new s or e will not cross array boundary
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (s + e) // 2
            if nums[mid] > nums[e]:
                # min in right half
                s = mid + 1
            else:
                # min in left half
                e = mid
        # print("min ", s)
        rot = s
        e = len(nums) - 1 + rot
        while s <= e:
            mid = (s + e) // 2
            r_mid = mid % len(nums)
            if target == nums[r_mid]:
                return r_mid
            elif target > nums[r_mid]:
                s = mid + 1
            else:
                e = mid - 1
        return -1


# @lc code=end
