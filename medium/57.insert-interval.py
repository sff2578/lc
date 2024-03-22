#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (39.23%)
# Likes:    9401
# Dislikes: 690
# Total Accepted:    912.8K
# Total Submissions: 2.3M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # newIntv_s <= cur_end: merge or insert, else: go to next
        # merge: newIntv_e > cur_s, else insert
        # O(n)
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        inserted, merged, merge_done, end_idx = False, False, False, -1
        for i in range(len(intervals)):
            if inserted:
                tmp = intervals[i]
                intervals[i] = cur_intv
                cur_intv = tmp
                if i == len(intervals) - 1:
                    intervals.append(cur_intv)
            elif merge_done:
                # if end_idx + 1 == i:
                #    # merge done, only add in new interval, no other merge is needed
                #    end_idx = len(intervals)
                #    break
                intervals[end_idx + 1] = intervals[i]
                end_idx += 1
            elif merged:
                if cur_intv[1] < intervals[i][0]:
                    merge_done = True
                    if end_idx + 1 == i:
                        # merge done, only add in new interval, no other merge is needed
                        end_idx = len(intervals)
                        break
                    else:
                        intervals[end_idx + 1] = intervals[i]
                        end_idx += 1

                else:
                    cur_intv[1] = max(cur_intv[1], intervals[i][1])
                    cur_intv[0] = min(cur_intv[0], intervals[i][0])
            else:
                cur_intv = intervals[i]
                if newInterval[0] <= cur_intv[1]:
                    # merge or insert
                    if newInterval[1] >= cur_intv[0]:
                        # merge
                        cur_intv[0] = min(cur_intv[0], newInterval[0])
                        cur_intv[1] = max(cur_intv[1], newInterval[1])
                        merged = True
                    else:
                        # insert before i
                        intervals[i] = newInterval
                        inserted = True
                        if i == len(intervals) - 1:
                            intervals.append(cur_intv)
                            return intervals
                end_idx += 1
        print(end_idx)
        count = len(intervals) - 1
        if not inserted:
            while count > end_idx:
                intervals.pop()
                count -= 1
        if not inserted and not merged:
            intervals.append(newInterval)
        return intervals


# @lc code=end
