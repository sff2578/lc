#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (37.72%)
# Likes:    167
# Dislikes: 31
# Total Accepted:    183.6K
# Total Submissions: 486.8K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their i^th paper and citations is sorted
# in ascending order, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is defined
# as the maximum value of h such that the given researcher has published at
# least h papers that have each been cited at least h times.
#
# You must write an algorithm that runs in logarithmic time.
#
#
# Example 1:
#
#
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.
#
#
# Example 2:
#
#
# Input: citations = [1,2,100]
# Output: 2
#
#
#
# Constraints:
#
#
# n == citations.length
# 1 <= n <= 10^5
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.
#
#
#


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        curCnt = 0
        # 0 1 2 3 4 5 6
        for i in range(len(citations) - 1, -1, -1):
            print(i, citations[i], curCnt)
            if curCnt < citations[i]:
                curCnt += 1
        return curCnt


# @lc code=end
