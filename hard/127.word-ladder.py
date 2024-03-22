#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (37.65%)
# Likes:    11654
# Dislikes: 1852
# Total Accepted:    1M
# Total Submissions: 2.6M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#

# @lc code=start
from string import ascii_lowercase as alc


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        def nexts(word):
            ret = []
            for i in range(len(word)):
                for char in alc:
                    new_w = word[:i] + char + word[i + 1 :]
                    if new_w in word_set:
                        ret.append(new_w)
            # print("word ", word, "nexts ", ret)
            return ret

        if endWord not in word_set:
            return 0
        step = dict({beginWord: 0})
        q = [beginWord]
        while q:
            # print("begin q: ", q)
            # print("begin step: ", step)
            cur = q.pop(0)
            for new_w in nexts(cur):
                if new_w == endWord:
                    return step[cur] + 1 + 1
                if new_w not in step:
                    q.append(new_w)
                    step[new_w] = step[cur] + 1
            # print("end q: ", q)
            # print("end step: ", step)
        return 0


# @lc code=end
