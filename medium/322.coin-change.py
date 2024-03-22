#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (42.57%)
# Likes:    18437
# Dislikes: 430
# Total Accepted:    1.7M
# Total Submissions: 3.9M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive, possible TLE if coins[i] ==1
        coins = sorted(coins, reverse=True)

        def recursive(amount) -> int:
            # return number of coins
            if amount == 0:
                return 0
            min_coins = inf
            found = False
            for coin in coins:
                if amount >= coin:
                    cur_coins = recursive(amount - coin)
                    if cur_coins >= 0:
                        cur_coins += 1
                        min_coins = min(min_coins, cur_coins)
                        found = True
            if not found:
                return -1
            return min_coins

        return recursive(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP, dp[amount+1], dp[i] mins min coins to compose amount=i
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_coins = inf
            found = False
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    min_coins = min(min_coins, dp[i - coin] + 1)
                    found = True
            if found:
                dp[i] = min_coins
        return dp[amount]


# @lc code=end
