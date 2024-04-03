#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (66.71%)
# Likes:    16603
# Dislikes: 832
# Total Accepted:    2.2M
# Total Submissions: 3.2M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
# Can you solve it without sorting?
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#


# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heapSol1(nums, k)

    def heapSol1(self, nums, k):
        # 1234567, k = 3
        # make use of the min-heap, construct a min heap of k elements, by using first k elements of array
        # go through array from k-end, push number and pop the smallest from heap, at end, heap will contain k largest number, heap[0] will be the smallest of the largets k elements
        heap = nums[:k]
        heapify(heap)
        for n in nums[k:]:
            heappushpop(heap, n)
        return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 03/30/2024 use quick sort, try to get the index of pivot, if
        # index == k-1, then we found it
        # TLE with last case, expected
        def partition(s, e):
            # sort descending
            pivot, l, r = nums[s], s, e
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                while l <= r and nums[l] >= pivot:
                    l += 1
                while l <= r and nums[r] <= pivot:
                    r -= 1
            nums[s], nums[r] = nums[r], nums[s]
            return r

        s, e = 0, len(nums) - 1
        while True:
            idx = partition(s, e)
            if idx == k - 1:
                return nums[idx]
            elif idx >= k:
                e = idx - 1
            else:
                s = idx + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 03/31/2024
        #  3 groups, 1,< than pivot, 2,== pivot, 3.large than pivot
        # if 1 >=k, check 1 again, if 2+3 < k check 3, otherwise return 2(which is pivot)
        pivot = nums[0]
        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))
        else:
            return pivot


# @lc code=end
