#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (40.25%)
# Likes:    2736
# Dislikes: 76
# Total Accepted:    125.3K
# Total Submissions: 311.2K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# You may recall that an array arr is a mountain array if and only if:
#
#
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such
# that:
#
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#
#
#
# Given an integer array arr, return the length of the longest subarray, which
# is a mountain. Return 0 if there is no mountain subarray.
#
#
# Example 1:
#
#
# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#
# Example 2:
#
#
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
#
#
#
# Follow up:
#
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
#
#
#


# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # i: start of sub, j: max of sub, cur
        i, j, res = 0, 0, 0
        for cur in range(1, len(arr)):
            if i == j:
                # this sub not started yet
                if arr[cur] <= arr[cur - 1]:
                    # previous i not start, try this one
                    i = j = cur
                else:
                    j = cur
            else:
                # in a sub
                if cur == j + 1:
                    # still looking for peek
                    if arr[cur] > arr[cur - 1]:
                        j = cur
                    elif arr[cur] == arr[cur - 1]:
                        # not a mountain, reset
                        i = j = cur
                else:
                    if arr[cur] >= arr[cur - 1]:
                        # cur is the end
                        res = max(res, cur - i)
                        if arr[cur] == arr[cur - 1]:
                            i = cur
                        else:
                            i = cur - 1
                        j = cur
        if len(arr) - 1 > j and j > i:
            res = max(res, (len(arr) - i))
        return res


# @lc code=end
