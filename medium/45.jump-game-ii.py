#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (40.01%)
# Likes:    12938
# Dislikes: 455
# Total Accepted:    954.9K
# Total Submissions: 2.4M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
#
#
# 0 <= j <= nums[i] and
# i + j < n
#
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
#
#
#


# @lc code=start
class Solution:
    # for each node, save all reachable node's minStep
    # Input: nums = [2,3,0,1,4]
    def jump(self, nums: List[int]) -> int:
        minSteps = [len(nums)] * len(nums)
        minSteps[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    minSteps[i + j] = min(minSteps[i + j], minSteps[i] + 1)
        return minSteps[-1]


# @lc code=end

# [2,3,1,1,4]
