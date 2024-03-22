#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (63.40%)
# Likes:    11191
# Dislikes: 128
# Total Accepted:    961.6K
# Total Submissions: 1.5M
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#


# @lc code=start
class Trie:
    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.start
        for i in range(len(word)):
            if not cur.next_m or word[i] not in cur.next_m:
                new_node = TrieNode()
                cur.next_m[word[i]] = new_node
            cur = cur.next_m[word[i]]
            if i == len(word) - 1:
                cur.end = True

    def search(self, word: str) -> bool:
        cur = self.start
        for i in range(len(word)):
            if not cur.next_m or word[i] not in cur.next_m:
                return False
            cur = cur.next_m[word[i]]
        if cur.next_m and not cur.end:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.start
        for i in range(len(prefix)):
            if not cur.next_m or prefix[i] not in cur.next_m:
                return False
            cur = cur.next_m[prefix[i]]
        return True


class TrieNode:
    def __init__(self, next_list=[]) -> None:
        self.next_m = dict()
        self.end = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
