#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.55%)
# Likes:    10035
# Dislikes: 529
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # start from f=0 s=1 t=len(nums)
        # if sum < target, move s forward, if sum > target, move t backward
        # once t moved backward, it doesn't need move forward again
        # if s meet t, move f one forward and s start with f+1 again
        nums.sort()
        # print(nums)
        min_diff, res = 2 * (10**4), nums[0] + nums[1] + nums[-1]
        for f in range(len(nums) - 2):
            s, t = f + 1, len(nums) - 1
            while s < t:
                cur_sum = nums[f] + nums[s] + nums[t]
                if abs(target - cur_sum) < min_diff:
                    res = cur_sum
                    min_diff = abs(target - cur_sum)
                if target - cur_sum == 0:
                    return cur_sum
                elif target - cur_sum > 0:
                    s += 1
                else:
                    t -= 1
        return res


# @lc code=end


# Sort the vector and then no need to run O(N^3) algorithm as each index has a direction to move.
#
# The code starts from this formation.
#
# ----------------------------------------------------
# ^  ^                                               ^
# |  |                                               |
# |  +- second                                     third
# +-first
# if nums[first] + nums[second] + nums[third] is smaller than the target, we know we have to increase the sum. so only choice is moving the second index forward.
#
# ----------------------------------------------------
# ^    ^                                             ^
# |    |                                             |
# |    +- second                                   third
# +-first
# if the sum is bigger than the target, we know that we need to reduce the sum. so only choice is moving 'third' to backward. of course if the sum equals to target, we can immediately return the sum.
#
# ----------------------------------------------------
# ^    ^                                          ^
# |    |                                          |
# |    +- second                                third
# +-first
# when second and third cross, the round is done so start next round by moving 'first' and resetting second and third.
#
# ----------------------------------------------------
#  ^    ^                                           ^
#  |    |                                           |
#  |    +- second                                 third
#  +-first
# while doing this, collect the closest sum of each stage by calculating and comparing delta. Compare abs(target-newSum) and abs(target-closest). At the end of the process the three indexes will eventually be gathered at the end of the array.
#
# ----------------------------------------------------
#                                         ^    ^    ^
#                                         |    |    `- third
#                                         |    +- second
#                                         +-first
# if no exactly matching sum has been found so far, the value in closest will be the answer.
