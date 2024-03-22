#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.86%)
# Likes:    16972
# Dislikes: 519
# Total Accepted:    1.1M
# Total Submissions: 3.1M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#


# -1 2 3 -2 4 -1
# @lc code=start
# [2,3,-2,4, -100]


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxProd, minProd = minProd, maxProd
            maxProd = max(nums[i], maxProd * nums[i])
            minProd = min(nums[i], minProd * nums[i])
            res = max(res, maxProd)
        return res


# if no neg, more the better
# if neg:
# if 0

# @lc code=end
