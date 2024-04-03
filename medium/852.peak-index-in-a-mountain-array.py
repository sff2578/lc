#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Medium (68.48%)
# Likes:    7324
# Dislikes: 1910
# Total Accepted:    785.8K
# Total Submissions: 1.1M
# Testcase Example:  '[0,1,0]'
#
# An array arr is a mountain if the following properties hold:
#
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#
#
#
# Given a mountain array arr, return the index i such that arr[0] < arr[1] <
# ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
#
# You must solve it in O(log(arr.length)) time complexity.
#
#
# Example 1:
#
#
# Input: arr = [0,1,0]
# Output: 1
#
#
# Example 2:
#
#
# Input: arr = [0,2,1,0]
# Output: 1
#
#
# Example 3:
#
#
# Input: arr = [0,10,5,2]
# Output: 1
#
#
#
# Constraints:
#
#
# 3 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
#
#
#


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 03/27/2024
        # compare mid-1, mid, mid+1
        s, e = 0, len(arr) - 1
        while s < e:
            mid = s + (e - s) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                e = mid
            else:
                s = mid + 1
        return -1


# @lc code=end
