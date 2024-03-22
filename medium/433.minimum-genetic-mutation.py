#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (52.69%)
# Likes:    2824
# Dislikes: 301
# Total Accepted:    147.7K
# Total Submissions: 277.2K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string startGene to a
# gene string endGene where one mutation is defined as one single character
# changed in the gene string.
#
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
#
#
# There is also a gene bank bank that records all the valid gene mutations. A
# gene must be in bank to make it a valid gene string.
#
# Given the two gene strings startGene and endGene and the gene bank bank,
# return the minimum number of mutations needed to mutate from startGene to
# endGene. If there is no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be
# included in the bank.
#
#
# Example 1:
#
#
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
#
#
# Example 2:
#
#
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
#
#
#
# Constraints:
#
#
# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C',
# 'G', 'T'].
#
#
#


# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # bank will create a graph, bfs on the graph
        # find all nexts which cur connect to, push next to queue if not visited already
        #   for each next or cur, keep the step to reach
        # 2 way to find all next of a node:
        #   1. compare each 2 nodes in bank and create a adj list if 2 nodes connected, O(n*n)
        #   2. from start, check all possible mutations of start in bank or not O(24*n)
        # if bank is big, 2 will be good, if bank small, 1 just overweigh 2 a little, so choose 2 in general
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        if endGene == startGene:
            return 0

        def validMut(cur):
            ret = []
            for i in range(len(cur)):
                for char in ["A", "C", "G", "T"]:
                    new_s = cur[:i] + char + cur[i + 1 :]
                    if new_s in bank_set:
                        ret.append(new_s)
            return ret

        q = [startGene]
        # visited = set()
        step = dict({startGene: 0})
        while q:
            cur = q.pop(0)
            for next in validMut(cur):
                if next == endGene:
                    return step[cur] + 1
                if next not in step:
                    step[next] = step[cur] + 1
                    q.append(next)
        return -1


# @lc code=end
