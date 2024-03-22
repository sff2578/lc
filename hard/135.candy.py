#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (41.20%)
# Likes:    6008
# Dislikes: 419
# Total Accepted:    336.7K
# Total Submissions: 817.5K
# Testcase Example:  '[1,0,2]'
#
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
#
#
# Example 1:
#
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two
# conditions.
#
#
#
# Constraints:
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#


# @lc code=start
# 1,5,3,2,4,6
# 0,1,0,0,1,2
# 0,2,1,0,0,0
# 0,3,1,0,1,2
# 1,3,2,1,2,2
# 1,0,2
# 0,0,1
#  1,0,1
# left-> right, if cur>pre, cur=prev+1, this cover increasing case
# right->left, descending case: if cur>next max(next+1,self)
# 1,0,2
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left, right = [0] * len(ratings), [0] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        hasZero = 0
        if left[len(ratings) - 1] == 0:
            hasZero = 1
        # print(left)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                left[i] = max(left[i + 1] + 1, left[i])
            if left[i] == 0:
                hasZero = 1
        # print(left)
        total = sum(left)
        if hasZero == 1:
            total += len(ratings)
        return total


# @lc code=end
