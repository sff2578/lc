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


# @lc code=end
