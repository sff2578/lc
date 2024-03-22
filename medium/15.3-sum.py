#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (32.97%)
# Likes:    29220
# Dislikes: 2655
# Total Accepted:    3.1M
# Total Submissions: 9.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort, add tuple to set to make sure unique
        # loop + 2 sum
        nums.sort()
        # print(nums)
        res = set()
        for i in range(0, len(nums) - 2):
            two_sum_res = self.twoSum(nums, i + 1, 0 - nums[i])
            for val1, val2 in two_sum_res:
                res.add((nums[i], val1, val2))
        return res

    def twoSum(self, nums, start, target):
        # print(start, target)
        rec = dict()
        res = set()
        for i in range(start, len(nums)):
            if nums[i] in rec.keys():
                res.add((nums[rec[nums[i]]], nums[i]))
            else:
                rec[target - nums[i]] = i
        # print(res)
        return res


# @lc code=end

#
# the key idea is the same as the TwoSum problem. When we fix the 1st number, the 2nd and 3rd number can be found following the same reasoning as TwoSum.
#
# The only difference is that, the TwoSum problem of LEETCODE has a unique solution. However, in ThreeSum, we have multiple duplicate solutions that can be found. Most of the OLE errors happened here because you could've ended up with a solution with so many duplicates.
#
# The naive solution for the duplicates will be using the STL methods like below :
#
# std::sort(res.begin(), res.end());
# res.erase(unique(res.begin(), res.end()), res.end());
# But according to my submissions, this way will cause you double your time consuming almostly.
#
# A better approach is that, to jump over the number which has been scanned, no matter it is part of some solution or not.
#
# If the three numbers formed a solution, we can safely ignore all the duplicates of them.
#
# We can do this to all the three numbers such that we can remove the duplicates.
# def threeSum(self, nums: List[int]) -> List[List[int]]:
#
# 	res = set()
#
# 	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
# 	n, p, z = [], [], []
# 	for num in nums:
# 		if num > 0:
# 			p.append(num)
# 		elif num < 0:
# 			n.append(num)
# 		else:
# 			z.append(num)
#
# 	#2. Create a separate set for negatives and positives for O(1) look-up times
# 	N, P = set(n), set(p)
#
# 	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
# 	#   i.e. (-3, 0, 3) = 0
# 	if z:
# 		for num in P:
# 			if -1*num in N:
# 				res.add((-1*num, 0, num))
#
# 	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
# 	if len(z) >= 3:
# 		res.add((0,0,0))
#
# 	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
# 	#   exists in the positive number set
# 	for i in range(len(n)):
# 		for j in range(i+1,len(n)):
# 			target = -1*(n[i]+n[j])
# 			if target in P:
# 				res.add(tuple(sorted([n[i],n[j],target])))
#
# 	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
# 	#   exists in the negative number set
# 	for i in range(len(p)):
# 		for j in range(i+1,len(p)):
# 			target = -1*(p[i]+p[j])
# 			if target in N:
# 				res.add(tuple(sorted([p[i],p[j],target])))
#
# 	return res
