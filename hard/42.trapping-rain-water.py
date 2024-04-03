#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (59.63%)
# Likes:    28410
# Dislikes: 401
# Total Accepted:    1.6M
# Total Submissions: 2.7M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    # find subarrays that both ends are higher than all others
    # Input: height = [4,2,0,3,2,5]
    def trap(self, height: List[int]) -> int:
        i, j, cur = 0, 0, 0
        ret = 0
        maxValIdx = [0] * len(height)
        maxSoFar = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] >= maxSoFar:
                maxValIdx[i] = i
                maxSoFar = height[i]
            else:
                maxValIdx[i] = maxValIdx[i + 1]
        while cur < len(height) - 1:
            print("cur", cur, "i", i, "j", j)
            # if next is higher, update j or start new subary
            if height[cur + 1] >= height[cur]:
                if i == cur:
                    i = cur + 1
                    j = i
                else:
                    j = cur + 1
                cur += 1
            else:
                # next lower, in this subary
                if j > i:
                    print("getting water", self.getWater(height, i, maxValIdx[i]))
                    ret += self.getWater(height, i, maxValIdx[i])
                    i = j = cur = maxValIdx[i]
        return ret

    def getWater(self, height, start, end):
        maxTotal = (end - start - 1) * min(height[start], height[end])
        for i in range(start + 1, end):
            maxTotal -= height[i]
        return maxTotal

    def trap(self, height: List[int]) -> int:
        # 04/01/2024
        # calculate for each column, total will be sum of all columns
        # each column, amount of water will be:
        #   min(maxL,maxR) - h[i]
        # two pointer from left and right to get maxL and maxR
        # the smaller pointer among(maxL,maxR) move forward(
        #   this is because the small one is bottleneck, we
        #   don't really care how max on the other side)
        # Input: height = [4,2,0,3,2,5]
        left, right, maxL, maxR = 0, len(height) - 1, height[0], height[-1]
        res = 0
        while left + 1 < right:
            # print(left, right)#
            if maxL <= maxR:
                # left move forward
                left += 1
                res += max(maxL - height[left], 0)
                maxL = max(maxL, height[left])
            else:
                # right move forward
                right -= 1
                res += max(maxR - height[right], 0)
                maxR = max(maxR, height[right])
            # print(maxL, maxR, res)
        return res


# @lc code=end
