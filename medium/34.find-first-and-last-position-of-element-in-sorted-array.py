#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.30%)
# Likes:    19915
# Dislikes: 483
# Total Accepted:    1.9M
# Total Submissions: 4.4M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
#
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # first seach for a occurance of target, if not found, return -1,-1, else, mark the index left_i = right_i = cur_i
        # when found target, do BS on both sides
        # left side: try to find first occurance, if not found, return -1, first occurance will be previous index
        #       always take left sub if a mid is target, update the left index to mid
        # right: try to find last occurance, if not found, -1, last occurance will be previous index
        #       always take right sub if a mid is target, update the right index to mid
        # [5,7,7,8,8,10]
        # [0,1,2,3,4,5]
        # [1] 1
        s, e = 0, len(nums) - 1
        met = -1
        ret = [-1, -1]
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                met = mid
                break
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        if met == -1:
            return ret
        ret = [met, met]
        # [5,7,7,8,8,10]
        # [0,1,2,3,4,5]
        # ret = 4,4

        # found a target, left side first
        # update ret[0] on each loop
        s, e = 0, met - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                ret[0] = mid
                e = mid - 1
            else:
                s = mid + 1
        # ret = 3,4
        # right side
        # update ret[1] on each loop
        # [5,7,7,8,8,10]
        # [0,1,2,3,4,5]
        # met = 4
        # ret = 3,4
        s, e = met + 1, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                ret[1] = mid
                s = mid + 1
            else:
                e = mid - 1

        return ret

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 03/22/2024
        # separatly search for first occurance and last occurance of target
        # for first occurance: if num < t: s=m+1, else: e=m(as m may be the first occurance).
        #   since e may not change, might have inifite loop when s==e and num >= t, so check s==e case separatly
        #   also this works because e=m is always updating e before s==e(mid will always go to the front)
        # for last occurance: split to <t =t >t 3 cases for simplicity

        # find first occur
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            num = nums[mid]
            if s == e and num == target:
                break
            elif s == e and num != target:
                # didnt found, return
                return [-1, -1]
            else:
                if num < target:
                    s = mid + 1
                else:
                    e = mid
        first = s
        s, e = 0, len(nums) - 1
        # at this point, we will for sure find target
        while s <= e:
            if s + 1 >= e:
                # this cover 1 number and 2 number case
                if nums[e] == target:
                    return [first, e]
                else:
                    return [first, s]
            mid = (s + e) // 2
            num = nums[mid]
            if num > target:
                e = mid - 1
            else:
                s = mid
        return [-1, -1]


# @lc code=end
