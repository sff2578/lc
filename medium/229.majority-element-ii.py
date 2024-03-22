#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (46.33%)
# Likes:    7856
# Dislikes: 354
# Total Accepted:    443K
# Total Submissions: 954.9K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
#
#
# Example 1:
#
#
# Input: nums = [3,2,3]
# Output: [3]
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow up: Could you solve the problem in linear time and in O(1) space?
#
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # initial candidate val doesn't matter
        cand1, cand2, count1, count2 = 0, 0, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 = 1
            elif count2 == 0:
                cand2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
        res = []
        if count1 > len(nums) / 3:
            res.append(cand1)
        if count2 > len(nums) / 3:
            res.append(cand2)
        return res


# @lc code=end
