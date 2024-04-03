#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (56.86%)
# Likes:    5887
# Dislikes: 738
# Total Accepted:    583.2K
# Total Submissions: 1M
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order and return
# it.
#
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.
#
#
# Example 1:
#
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not
# changed (for example, 2 and 3), while the positions of other numbers are
# changed (for example, 1 and 5).
#
#
# Example 2:
#
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
#
#
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 03/29/2024
        # merge sort, divid and conquer
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        def merge(left, right):
            l_idx, r_idx = 0, 0
            ret = []
            while l_idx < len(left) and r_idx < len(right):
                if left[l_idx] <= right[r_idx]:
                    ret.append(left[l_idx])
                    l_idx += 1
                else:
                    ret.append(right[r_idx])
                    r_idx += 1

            while l_idx < len(left):
                ret.append(left[l_idx])
                l_idx += 1

            while r_idx < len(right):
                ret.append(right[r_idx])
                r_idx += 1
            return ret

        return merge(left, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        # 03/29/2024 quick sort
        # find a pivot, move all smaller to left and bigger to right
        # switch the last smaller one with pivot,then pivot is in place
        # recursive for 2 halfs
        self.quick_sort_helper(nums, 0, len(nums) - 1)
        return nums
        # return self.quickSort(nums)

    def quick_sort_helper(self, nums, s, e):
        # s, e inclusive
        # print(s, e)
        if s >= e:
            return
        # pivot = nums[s + (e - s) // 2]
        pivot = nums[e]
        i, j = s, e
        while j >= i:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if j >= i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        self.quick_sort_helper(nums, s, j)
        self.quick_sort_helper(nums, i, e)

    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail:
                return
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot:
                    l += 1
                while r >= l and nums[r] > pivot:
                    r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums) - 1)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        # 03/30/2024
        return self.qs_imp2(nums, 0, len(nums) - 1)

    def qs_imp2(self, nums, s, e):
        if s < 0 or e >= len(nums) or s > e:
            return
        pivot, l, r = nums[s], s + 1, e
        while l <= r:
            if nums[l] > pivot and nums[r] < pivot:
                nums[l], nums[r] = nums[r], nums[l]
            while l <= r and nums[l] <= pivot:
                l += 1
            while l <= r and nums[r] >= pivot:
                r -= 1
        nums[s], nums[r] = nums[r], nums[s]
        self.qs_imp2(nums, s, r - 1)
        self.qs_imp2(nums, l, e)
        return nums


# @lc code=end
