#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (45.74%)
# Likes:    16808
# Dislikes: 745
# Total Accepted:    1.6M
# Total Submissions: 3.4M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP, dp[i] for each char in s
        # dp[i] set to True if s[k:i+1] is a word in wordDict and dp[k-1] is true(meaning another word end at k-1)
        # dp[-1] is True
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and (
                    i - len(word) == -1 or dp[i - len(word)]
                ):
                    dp[i] = True
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # use Trie, create a Trie with wordDict
        # recursively, given a string and trie, check if first n char can form a word in Trie.
        #   if yes, recursively do with rest of string and same Trie
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        def recursive(s, trie):
            if s == "":
                return True
            cur = trie.root
            for i in range(len(s)):
                c = s[i]
                cur = cur.next_m.get(c, None)
                if not cur:
                    return False
                if cur.is_word:
                    if recursive(s[i + 1 :], trie):
                        return True
            return False

        return recursive(s, trie)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.next_m:
                new_node = TrieNode()
                cur.next_m[c] = new_node
            cur = cur.next_m[c]
        cur.is_word = True


class TrieNode:
    def __init__(self) -> None:
        self.next_m = dict()
        self.is_word = False


# @lc code=end
