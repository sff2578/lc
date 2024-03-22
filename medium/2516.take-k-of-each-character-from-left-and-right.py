#
# @lc app=leetcode id=2516 lang=python3
#
# [2516] Take K of Each Character From Left and Right
#
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
#
# algorithms
# Medium (34.43%)
# Likes:    597
# Dislikes: 55
# Total Accepted:    12.2K
# Total Submissions: 35.5K
# Testcase Example:  '"aabaaaacaabc"\n2'
#
# You are given a string s consisting of the characters 'a', 'b', and 'c' and a
# non-negative integer k. Each minute, you may take either the leftmost
# character of s, or the rightmost character of s.
#
# Return the minimum number of minutes needed for you to take at least k of
# each character, or return -1 if it is not possible to take k of each
# character.
#
#
# Example 1:
#
#
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation:
# Take three characters from the left of s. You now have two 'a' characters,
# and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters,
# two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.
#
#
# Example 2:
#
#
# Input: s = "a", k = 1
# Output: -1
# Explanation: It is not possible to take one 'b' or 'c' so return -1.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only the letters 'a', 'b', and 'c'.
# 0 <= k <= s.length
#
#
#


# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Input: s = "aabaaaacaabc", k = 2
        # Input: s = "baaaaaacaabc", k = 2
        # thought: take longest substring, after that still matches that each a,b,c count > k
        # longest substr: sliding window, left pointer start with 0, right pointer keeps going right, substring keeps increase, record the length, until the remaining str not match, then shrink window by moving left pointer right, until meet criteria, once we come to a char and caused remaining doesn't meet criteria, meaning the next possible substring have to start from this char
        cntMap = dict()
        cntMap["a"] = s.count("a")
        cntMap["b"] = s.count("b")
        cntMap["c"] = s.count("c")
        if cntMap["a"] < k or cntMap["b"] < k or cntMap["c"] < k:
            return -1
        maxSub = 0
        left = 0
        curCnt = 0
        for char in s:
            cntMap[char] -= 1
            curCnt += 1
            while cntMap["a"] < k or cntMap["b"] < k or cntMap["c"] < k:
                cntMap[s[left]] += 1
                left += 1
                curCnt -= 1
            maxSub = max(maxSub, curCnt)
        return len(s) - maxSub


# @lc code=end
