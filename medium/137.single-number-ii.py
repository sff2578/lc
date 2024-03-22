#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (61.25%)
# Likes:    7632
# Dislikes: 671
# Total Accepted:    553.2K
# Total Submissions: 889.9K
# Testcase Example:  '[2,2,3,2]'
#
# Given an integer array nums where every element appears three times except
# for one, which appears exactly once. Find the single element and return it.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
#
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each element in nums appears exactly three times except for one element which
# appears once.
#
#
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for each bit, it will occur either 3n times or 3n+1 time
        # so look at each bit, if it's 3n+1 times, it is part of single number
        # O(n) space and O(32n) time
        # fix1 neg: first loop to check if final is neg or pos
        res = 0
        neg_cnt = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                neg_cnt += 1
        for i in range(32):
            cur_cnt = 0
            for k in range(len(nums)):
                # print(
                #    "num ",
                #    nums[k],
                #    "num&1",
                #    bin(nums[k] & 0b11111111111111111111111111111111),
                # )
                cur_cnt += nums[k] & 1
                nums[k] >>= 1
                # print("after shift", num)
            if cur_cnt % 3:
                # print("curcnt", cur_cnt)
                # occurs 3n+1 time, use this bit as 1
                res += 1 << i
        if neg_cnt % 3:
            res = -res
        return res

    def singleNumber(self, nums: List[int]) -> int:
        # ones 1: the bit that only occurs 1 time
        # twos 1: the bit that only occurs 2 time
        # if occur 3 time, ones and twos are both 0
        # iif ocur 4 time, same as 1 time, 5 time same as 2 time
        ones, twos = 0, 0
        for num in nums:
            twos = twos | (
                num & ones
            )  # now twos include bits occured 2times and 3times
            ones = ones ^ num  # now ones include bits occured 1times and 3times
            threes = ones & twos
            twos = twos & (~threes)
            ones = ones & (~threes)
        return ones

    """
    1xxxx0010 -2
    1xxxx0010 -2
    0xxxx0001 1
    0xxxx0001 1
    0xxxx0100 4
    0xxxx0001 1
    0xxxx0100 4
    0xxxx0100 4
    1xxxx0100 -4
    1xxxx0010 -2
    xxxxx0100
    """


# @lc code=end
