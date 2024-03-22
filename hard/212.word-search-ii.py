#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (36.12%)
# Likes:    9146
# Dislikes: 435
# Total Accepted:    620.6K
# Total Submissions: 1.7M
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#


# create a Trie tree to save words
# dfs
# for a given cordinator, recursivly look at each neighbor, go until all 4 neighbors can not
#   form a word. otherwise return each word we encounter
# keep a visited set, add to set before looking into neighbors and remove from set after dfs return
# keep a ret set to avoid duplicate
# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ret_set = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValidCord(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            return True

        def dfs(cord, root: TrieNode, visited, cur_word):
            if cord in visited:
                return
            letter = board[cord[0]][cord[1]]
            if letter not in root.next_map:
                return
            next_root = root.next_map[letter]
            cur_word += letter
            if next_root.is_word:
                ret_set.add(cur_word)
            visited.add(cord)
            for dir in directions:
                i, j = cord[0] + dir[0], cord[1] + dir[1]
                if not isValidCord(i, j):
                    continue
                dfs((i, j), next_root, visited, cur_word)
            visited.remove(cord)
            cur_word = cur_word[: len(cur_word) - 1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                cord, visited, cur_word = (i, j), set(), ""
                dfs(cord, trie.root, visited, cur_word)

        return list(ret_set)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.next_map:
                new_node = TrieNode()
                cur.next_map[char] = new_node
            cur = cur.next_map[char]
            if i == len(word) - 1:
                cur.is_word = True
        return


class TrieNode:
    def __init__(self) -> None:
        self.is_word = False
        self.next_map = dict()


# @lc code=end
