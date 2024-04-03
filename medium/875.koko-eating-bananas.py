#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (48.98%)
# Likes:    10111
# Dislikes: 589
# Total Accepted:    599.5K
# Total Submissions: 1.2M
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
#
#
# Example 1:
#
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
#
# Example 2:
#
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
#
# Example 3:
#
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
#
#
#

from math import ceil


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 03/27/2024
        # speed minimal is min(piles) and max is max(piles)
        #   because even if eats more that max(piles), each hour can not
        #   each from 2 piles
        # O(k) where k is max from ary

        # get min and max from piles
        lrg = piles[0]
        for num in piles:
            lrg = max(lrg, num)

        # function to get hours needed to finish
        def hours(speed):
            needed = 0
            for num in piles:
                needed += ceil(num / speed)
            return needed

        # binary search to get the speed
        sml = 1
        while sml < lrg:
            mid = (sml + lrg) // 2
            if hours(mid) <= h:
                # self or left
                lrg = mid
            else:
                sml = mid + 1
        return sml


# @lc code=end
