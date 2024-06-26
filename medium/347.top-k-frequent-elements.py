#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.72%)
# Likes:    16935
# Dislikes: 630
# Total Accepted:    2M
# Total Submissions: 3.2M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

import collections


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use more space, num: freq and freq: num
        # freq: num use array
        freq = collections.Counter(nums)
        ary = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            ary[count].append(num)
        res = []
        for i in range(len(ary) - 1, -1, -1):
            for num in ary[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    break
        return res


# @lc code=end
