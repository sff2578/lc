#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (46.38%)
# Likes:    21438
# Dislikes: 740
# Total Accepted:    2.2M
# Total Submissions: 4.7M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort: sorted(lis, key=lambda x: x[0])
        # for each intv, go through ret list and merge if possible, add if not
        # merge: my_start <= o_end and my_end >= o_start
        # worse n square
        intervals = sorted(intervals, key=lambda x: x[0])
        # print("sore ", intervals)
        ret = []
        for intv in intervals:
            found = False
            for new_intv in ret:
                if intv[0] <= new_intv[1] and intv[1] >= new_intv[0]:
                    # print("before ", ret)
                    self.merge_helper(intv, new_intv)
                    # print("after ", ret)
                    found = True
                    break
            if not found:
                ret.append(intv)
        return ret

    def merge_helper(self, intv, target_intv):
        target_intv[0] = min(intv[0], target_intv[0])
        target_intv[1] = max(intv[1], target_intv[1])

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 04/05/2024
        # new interval list
        # check end of new list overlap with next interval?
        #   yes: merge and replace, no: append
        intervals = sorted(intervals, key=lambda x: x[0])

        def overlap(itv1, itv2):
            return itv1[1] >= itv2[0]

        def merge(itv1, itv2):
            return [itv1[0], max(itv1[1], itv2[1])]

        ret = [intervals[0]]
        for interval in intervals:
            if overlap(ret[-1], interval):
                new_interval = merge(ret[-1], interval)
                ret[-1] = new_interval
            else:
                ret.append(interval)
        return ret


# [[2,3],[4,5],[6,7],[8,9],[1,10]]

# @lc code=end
