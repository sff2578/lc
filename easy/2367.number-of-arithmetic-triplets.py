#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#
# https://leetcode.com/problems/number-of-arithmetic-triplets/description/
#
# algorithms
# Easy (83.35%)
# Likes:    1149
# Dislikes: 65
# Total Accepted:    101K
# Total Submissions: 120.9K
# Testcase Example:  '[0,1,4,6,7,10]\n3'
#
# You are given a 0-indexed, strictly increasing integer array nums and a
# positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the
# following conditions are met:
#
#
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
#
#
# Return the number of unique arithmetic triplets.
#
#
# Example 1:
#
#
# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 ==
# 3.
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,8,9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 ==
# 2.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 200
# 0 <= nums[i] <= 200
# 1 <= diff <= 50
# nums is strictly increasing.
#
#
#


# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # just make sure cur, cur+diff, cur+diff*2 in array
        nums_set = set(nums)
        res = 0
        # print(nums[:-2])
        for num in nums[:-2]:
            if (num + diff) in nums_set and (num + 2 * diff) in nums_set:
                res += 1
        return res


# @lc code=end
