#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (47.24%)
# Likes:    7988
# Dislikes: 658
# Total Accepted:    525K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
#
# An integer a is closer to x than an integer b if:
#
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
#
#
#

from collections import deque


# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 3/25/2024
        # find x, or the place around where x can be inserted
        # go left and right and find the closest, if left, append left, if right append right, use deque to save time
        # find pivot
        s, e = 0, len(arr) - 1
        while s < e:
            mid = (s + e) // 2
            if arr[mid] == x:
                s = mid
                break
            elif arr[mid] < x:
                s = mid + 1
            else:
                e = mid - 1
        # now s is the pivot point
        l_cnt, r_cnt, l_idx, r_idx = 0, 0, 0, 0
        ret = deque()
        if arr[s] == x:
            l_cnt += 1
            ret.append(arr[s])
            l_idx = s - 1
            r_idx = s + 1
        elif arr[s] < x:
            l_idx = s
            r_idx = s + 1
        else:
            l_idx = s - 1
            r_idx = s
        while l_cnt + r_cnt < k:
            l_diff, r_diff = inf, inf
            if l_idx >= 0:
                l_diff = abs(arr[l_idx] - x)
            if r_idx < len(arr):
                r_diff = abs(arr[r_idx] - x)
            if l_diff <= r_diff:
                l_cnt += 1
                ret.appendleft(arr[l_idx])
                l_idx -= 1
            else:
                r_cnt += 1
                ret.append(arr[r_idx])
                r_idx += 1
        return list(ret)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 03/26/2024
        # binary search to find the start element of return list
        # 123456
        # the start element will be [s, e-k+1] inclusive
        # if x is alreay too far from right side, then the start
        #  should move left(it's okay this might already be the fix)
        # if x is already too far from left side, then the start
        #  should move right
        # until there's only 1 number left and this is the start
        # 123456 4 -1
        # [1,2,3,4,5] 4 3
        s, e = 0, len(arr) - k
        while s < e:
            mid = (s + e) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                # too far to right, go left
                e = mid
            else:
                s = mid + 1
        return arr[s : s + k]

    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #    # answer
    #    left = 0
    #    right = len(arr) - k

    #    while left < right:
    #        mid = left + (right - left) // 2

    #        if x - arr[mid] > arr[mid + k] - x:
    #            left = mid + 1
    #        else:
    #            right = mid
    #    return arr[left : left + k]


# @lc code=end
