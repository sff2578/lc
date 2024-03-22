#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (66.80%)
# Likes:    17991
# Dislikes: 540
# Total Accepted:    2.5M
# Total Submissions: 3.6M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m_map = dict()
        for str in strs:
            key = self.strToKey(str)
            if key not in m_map.keys():
                m_map[key] = [str]
            else:
                m_map[key].append(str)
        ret = []
        for key in m_map.keys():
            ret.append(m_map[key])
        return ret

    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        if len(s) != len(t):
            return False
        for char in t:
            if s_map[char] == 0:
                return False
            s_map[char] -= 1
        return True

    def strToKey(self, s):
        m_map = Counter(s)
        key_list = list(m_map.keys())
        key_list.sort()
        ret = ""
        for key in key_list:
            ret += key + str(m_map[key])
        return ret


# @lc code=end
