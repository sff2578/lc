#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.98%)
# Likes:    27432
# Dislikes: 3024
# Total Accepted:    2.4M
# Total Submissions: 6.1M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # partition the smaller array X, and get corresponding elems from Y, to find the partition location where all [left X, left Y] are less than [right X, right Y], if not, go left on X or right on Y depends.
        # loop end case: while s <= e, remember, if input is valide, i.e. both array are sorted, we'll always find a solution before s goes > than e.
        # edge case: 0 or len of X and Y. consider invalid case as -INF and INF, will simplify the comparision
        # trick: use s/e and the partition location, e.g. for array [1,2,3], there are 4 possible partitions, 0(not use X at all), 1(use 1 of X), 2(use 2 of X), 3(use 3 which is all of X). to get the number, need to do X[s-1], otherwise hard to cover all cases with 1 line of code to get the current element. in this case X[0] = -INF, x[3] = INF
        x, y = len(nums1), len(nums2)
        # make sure nums1 is always smaller
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)
        s, e = 0, len(nums1)
        while s <= e:
            mX = (s + e) // 2
            mY = (x + y + 1) // 2 - mX

            xL = -inf if mX == 0 else nums1[mX - 1]
            yL = -inf if mY == 0 else nums2[mY - 1]
            xR = inf if mX == x else nums1[mX]
            yR = inf if mY == y else nums2[mY]
            if xL <= yR and yL <= xR:
                # found the right partition, get median
                if (x + y) % 2 == 1:
                    return max(xL, yL)
                else:
                    return (max(xL, yL) + min(xR, yR)) / 2
            if xL > yR:
                # take too much X
                e = mX - 1
            else:
                # take too less X
                s = mX + 1
        return -1


# @lc code=end
