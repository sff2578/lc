#
# @lc app=leetcode id=2517 lang=python3
#
# [2517] Maximum Tastiness of Candy Basket
#
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/
#
# algorithms
# Medium (64.91%)
# Likes:    807
# Dislikes: 105
# Total Accepted:    16.3K
# Total Submissions: 25.9K
# Testcase Example:  '[13,5,1,8,21,2]\n3'
#
# You are given an array of positive integers price where price[i] denotes the
# price of the i^th candy and a positive integer k.
#
# The store sells baskets of k distinct candies. The tastiness of a candy
# basket is the smallest absolute difference of the prices of any two candies
# in the basket.
#
# Return the maximum tastiness of a candy basket.
#
#
# Example 1:
#
#
# Input: price = [13,5,1,8,21,2], k = 3
# Output: 8
# Explanation: Choose the candies with the prices [13,5,21].
# The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) =
# min(8, 8, 16) = 8.
# It can be proven that 8 is the maximum tastiness that can be achieved.
#
#
# Example 2:
#
#
# Input: price = [1,3,1], k = 2
# Output: 2
# Explanation: Choose the candies with the prices [1,3].
# The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
# It can be proven that 2 is the maximum tastiness that can be achieved.
#
#
# Example 3:
#
#
# Input: price = [7,7,7,7], k = 2
# Output: 0
# Explanation: Choosing any two distinct candies from the candies we have will
# result in a tastiness of 0.
#
#
#
# Constraints:
#
#
# 2 <= k <= price.length <= 10^5
# 1 <= price[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # how to see x is the min diff: starting from smallest, if next one - cur one > x, put next one in subset.
        # min diff between a given number and all numbers in a subset will be the given number and the largest one of subset
        price.sort()
        start, end = 0, 10**9
        while start < end:
            # print(start, end)
            cur = (end + start) // 2
            if self.check(cur, k, price):
                # this val is ok, check all vals after this one
                start = cur + 1
            else:
                end = cur
        return start - 1

    def check(self, x, k, price):
        last, count = price[0], 1
        for curPrice in price:
            if curPrice - last >= x:
                last = curPrice
                count += 1
            if count == k:
                # print("check ", x, True)
                return True
        # print("check ", x, False)
        return False


# Intuition
# We can use binary search to search the minimum difference. Since range is 0 - 10^9, Time complexity will be n * log(10 ^ 9) = 10 ^ 5 * 30. This should be within constraints.
#
# Approach
# Sort prices
# Run a binary search in the range 0 to 10 ^ 9
# The check function iterates over the array prices and checks if the given value x can be the minimum difference for any subsequence of the array prices

# The difficult and interesting part of this question is to figure out that we can turn this optimization problem into a decision problem.
#
# If we choose an arbitrary value x the decision is whether this number can satify the problem condition. We need to figure out if x can be the minimum difference of k chosen candies.
#
# If x = 5 satisfies the condition, then we also know for fact that x = 4 will work, because smaller difference is also contained within the bigger diference. This turns our search space into a monotonic one. Because whenever we find a number x that doesn't satify the condition anymore, all greater values won't work too. The search space will look like this: [T, T, T, F, F], where T stands for true (satisfying the condition) and F stands for false.
#
# Given that intuition, we can perform a binary search to find the best x.
# def maximumTastiness(self, price: List[int], k: int) -> int:
#    price.sort()
#    def check(x):
#        last, count, i = price[0], 1, 1
#        while count < k and i < len(price):
#            if price[i] - last >= x:
#                last, count = price[i], count + 1
#            i += 1
#        return count == k
#    lo, hi = 0, 10 ** 9
#    while lo < hi:
#        mid = (lo + hi) // 2
#        if check(mid): lo = mid + 1
#        else: hi = mid
#    return lo - 1


# @lc code=end
