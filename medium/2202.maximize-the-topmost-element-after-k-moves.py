#
# @lc app=leetcode id=2202 lang=python3
#
# [2202] Maximize the Topmost Element After K Moves
#
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/description/
#
# algorithms
# Medium (22.80%)
# Likes:    560
# Dislikes: 302
# Total Accepted:    24.5K
# Total Submissions: 107.5K
# Testcase Example:  '[5,2,2,4,0,6]\n4'
#
# You are given a 0-indexed integer array nums representing the contents of a
# pile, where nums[0] is the topmost element of the pile.
#
# In one move, you can perform either of the following:
#
#
# If the pile is not empty, remove the topmost element of the pile.
# If there are one or more removed elements, add any one of them back onto the
# pile. This element becomes the new topmost element.
#
#
# You are also given an integer k, which denotes the total number of moves to
# be made.
#
# Return the maximum value of the topmost element of the pile possible after
# exactly k moves. In case it is not possible to obtain a non-empty pile after
# k moves, return -1.
#
#
# Example 1:
#
#
# Input: nums = [5,2,2,4,0,6], k = 4
# Output: 5
# Explanation:
# One of the ways we can end with 5 at the top of the pile after 4 moves is as
# follows:
# - Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
# - Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
# - Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
# - Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
# Note that this is not the only way to end with 5 at the top of the pile. It
# can be shown that 5 is the largest answer possible after 4 moves.
#
#
# Example 2:
#
#
# Input: nums = [2], k = 1
# Output: -1
# Explanation:
# In the first move, our only option is to pop the topmost element of the pile.
# Since it is not possible to obtain a non-empty pile after one move, we return
# -1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i], k <= 10^9
#
#
#


# @lc code=start
class Solution:
    # use k-th number or not (last option get or put)
    # use: res = nums[k-1]
    # no: last option must be put back, so we'll put bac
    #   largest number of first k-1th numbers: max(nums[k-2])
    # if k=len, last option can only be put back, so set last number to -1
    # if k > len: last number can be last number of nums(last option get)
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k % 2 != 0:
            return -1
        if k == 0:
            return nums[0]
        maxD = 0
        last = 0
        if k == len(nums):
            last = -1
        elif k > len(nums):
            last = nums[len(nums) - 1]
        else:
            last = nums[k]
        for i in range(k - 1):
            if i >= len(nums):
                return max(maxD, last)
            maxD = max(maxD, nums[i])
        # if k % 2 == 1 and k < len(nums):
        #    return max(maxD, nums[k])
        return max(maxD, last)


# @lc code=end
