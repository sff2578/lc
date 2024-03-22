#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (41.67%)
# Likes:    6988
# Dislikes: 920
# Total Accepted:    635.9K
# Total Submissions: 1.5M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # pattern to s map and s to pattern map
        s_ary = s.split()
        if len(pattern) != len(s_ary):
            return False
        p_to_s, s_to_p = dict(), dict()
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in p_to_s.keys():
                p_to_s[char] = s_ary[i]
                if s_ary[i] in s_to_p.keys() and s_to_p[s_ary[i]] != char:
                    return False
                else:
                    s_to_p[s_ary[i]] = char
            else:
                if p_to_s[char] != s_ary[i]:
                    return False
        return True


# @lc code=end
