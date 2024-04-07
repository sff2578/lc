#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (71.47%)
# Likes:    5476
# Dislikes: 110
# Total Accepted:    401.3K
# Total Submissions: 560.8K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list
# of intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.
# 
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].
# 
# 
# Example 1:
# 
# 
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 
# 
# Example 2:
# 
# 
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10^9
# endi < starti+1
# 0 <= startj < endj <= 10^9 
# endj < startj+1
# 
# 
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 04/06/2024
        # similar with solution1 of 253 meeting rooms ii
        # start array and end array
        # if s<=e meeting +1, if e < s meeting -1
        # if meeting == 2, record start, if meeting == 1 record end
        start = sorted([x[0] for x in firstList+secondList])
        end = sorted([x[1] for x in firstList+secondList])
        ret = []
        cnt = i = j = 0
        while i < len(start) or j < len(end):
            if i < len(start) and start[i] <= end[j]:
                cnt += 1
                if cnt == 2:
                    ret.append([start[i], 0])
                i += 1
            else:
                cnt -= 1
                if cnt == 1:
                    ret[-1][1] = end[j]
                j += 1
        return ret
        
        
# @lc code=end

