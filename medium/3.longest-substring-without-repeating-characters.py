#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.89%)
# Likes:    38073
# Dislikes: 1742
# Total Accepted:    5.2M
# Total Submissions: 15.2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#
# abcacefg
# xxx34567
# abcc
# aaa
# x1


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use set, if not in map, add to map, fast++, if in map, slow move to next, keep max size each time
        my_set = dict()
        fast, slow = 0, 0
        res = 0
        while fast < len(s):
            cur_char = s[fast]
            if cur_char not in my_set.keys():
                # not in set
                my_set[cur_char] = fast
                res = max(res, fast - slow + 1)
                fast += 1
            else:
                # in set
                existing = my_set[cur_char]
                while slow <= existing:
                    my_set.pop(s[slow])
                    slow += 1

        return res


# @lc code=end
