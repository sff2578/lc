#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#
# https://leetcode.com/problems/jump-game-iii/description/
#
# algorithms
# Medium (63.99%)
# Likes:    3851
# Dislikes: 93
# Total Accepted:    198.7K
# Total Submissions: 310.5K
# Testcase Example:  '[4,2,3,0,3,1,2]\n5'
#
# Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i]
# or i - arr[i], check if you can reach any index with value 0.
#
# Notice that you can not jump outside of the array at any time.
#
#
# Example 1:
#
#
# Input: arr = [4,2,3,0,3,1,2], start = 5
#               f,t,f,t,f,f,f
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
#
#
# Example 2:
#
#
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
#
#
# Example 3:
#
#
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
#
#
#
# 1,1,1,1,0 - 2
# f,f,t,f,f-2
# f,f,t,t,f-3
# f,f,t,t,t-4
# f,f,t,t,t-2
# f,t,t,t,t-1
# t,t,t,t,t-0


# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        finalAry = [False] * len(arr)
        finalAry[start] = True
        self.canReachHelper(arr, start, finalAry)
        for i in range(len(arr)):
            if arr[i] == 0:
                if finalAry[i] == True:
                    return True
        return False

    def canReachHelper(self, arr, start, resAry):
        # print("round:", start, resAry)
        if arr[start] == 0:
            resAry[start] = True
            return
        nextIdx = start + arr[start]
        prevIdx = start - arr[start]
        if nextIdx < len(arr) and resAry[nextIdx] == False:
            resAry[nextIdx] = True
            self.canReachHelper(arr, nextIdx, resAry)
        if prevIdx >= 0 and resAry[prevIdx] == False:
            resAry[prevIdx] = True
            self.canReachHelper(arr, prevIdx, resAry)


# @lc code=end
