#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (44.21%)
# Likes:    7395
# Dislikes: 434
# Total Accepted:    598.8K
# Total Submissions: 1.3M
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#'[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
#
#
#
# Example:
#
#
# Input
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.
#
#
#


# @lc code=start
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if not cur.followings or word[i] not in cur.followings:
                new_node = TrieNode()
                cur.followings[word[i]] = new_node
            cur = cur.followings[word[i]]
            if i == len(word) - 1:
                cur.is_word = True

    def search(self, word: str) -> bool:
        # must be a exact match
        def dfs(root, s_idx):
            cur = root
            for i in range(s_idx, len(word)):
                # print("checking char: ", word[i])
                if word[i] != ".":
                    if word[i] not in cur.followings:
                        return (False, None)
                    cur = cur.followings[word[i]]
                    # print("cur: ", cur)
                else:
                    ret = False
                    for _, next in cur.followings.items():
                        (ret, ret_cur) = dfs(next, i + 1)
                        # print("dfs return ret: ", ret, "end pointer: ", ret_cur)
                        if ret:
                            break
                    if not ret:
                        return (False, None)
                    else:
                        cur = ret_cur
                        break
            if cur.is_word:
                return (True, cur)
            return (False, None)

        return dfs(self.root, 0)[0]


class TrieNode:
    def __init__(self) -> None:
        self.is_word = False
        self.followings = dict()


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
