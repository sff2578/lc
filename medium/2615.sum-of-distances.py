#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#
# https://leetcode.com/problems/sum-of-distances/description/
#
# algorithms
# Medium (30.01%)
# Likes:    550
# Dislikes: 73
# Total Accepted:    13.8K
# Total Submissions: 46.1K
# Testcase Example:  '[1,3,1,1,2]'
#
# You are given a 0-indexed integer array nums. There exists an array arr of
# length nums.length, where arr[i] is the sum of |i - j| over all j such that
# nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
#
# Return the array arr.
#
#
# Example 1:
#
#
# Input: nums = [1,3,1,1,2]
# Output: [5,0,3,4,0]
# Explanation:
# When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0
# - 2| + |0 - 3| = 5.
# When i = 1, arr[1] = 0 because there is no other index with value 3.
# When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2
# - 0| + |2 - 3| = 3.
# When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3
# - 0| + |3 - 2| = 4.
# When i = 4, arr[4] = 0 because there is no other index with value 2.
#
#
#
# Example 2:
#
#
# Input: nums = [0,5,3]
# Output: [0,0,0]
# Explanation: Since each element in nums is distinct, arr[i] = 0 for all
# i.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_map = dict()
        index_total = dict()
        cnt_map = dict()

        for i in range(len(nums)):
            if nums[i] in index_map:
                index_map[nums[i]].append(i)
            else:
                index_map[nums[i]] = [i]
        for key, ary in index_map.items():
            total_index = []
            cur = 0
            for val in ary:
                cur += val
                total_index.append(cur)
            index_total[key] = total_index
            cnt_map[key] = 0

        res = []
        # print(index_total)
        for i in range(len(nums)):
            cnt = cnt_map[nums[i]]
            total = len(index_total[nums[i]])
            total_idx_ary = index_total[nums[i]]
            val = (
                i * cnt
                - (total_idx_ary[cnt] - i)
                + total_idx_ary[-1]
                - total_idx_ary[cnt]
                - i * (total - 1 - cnt)
            )
            res.append(val)
            cnt_map[nums[i]] += 1
        return res


# @lc code=end
