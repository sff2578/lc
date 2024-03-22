#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (46.13%)
# Likes:    15684
# Dislikes: 651
# Total Accepted:    1.4M
# Total Submissions: 3.1M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return true if you can finish all courses. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#
#


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.canFinish_dfs(numCourses, prerequisites)

    def canFinish_khan(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # khan's algorithm on topo sort
        # create 2 hashmap on both directions: node: [prereq of this node]  and node:[destination of cur node]
        # ok_set: all nodes that can be reached
        # pop from ok_set, find the destinations of this node, and remove current node from the prereq of destination node
        # if no prereq anymore, add destination to ok_set, remove dest node from first map
        # if empty ok_set, check if first map is empty
        map1, map2 = defaultdict(list), defaultdict(list)
        for dest, pre in prerequisites:
            map1[dest].append(pre)
            map2[pre].append(dest)
        # print(map1, map2)

        reached_lsit = []
        for node in range(numCourses):
            pre_list = map1[node]
            if not pre_list:
                del map1[node]
                reached_lsit.append(node)
        while reached_lsit:
            cur = reached_lsit.pop(0)
            for dest in map2[cur]:
                map1[dest].remove(cur)
                if not map1[dest]:
                    reached_lsit.append(dest)
                    del map1[dest]
        if len(map1) == 0:
            return True
        else:
            return False

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map of node:[dest nodes from cur node]
        # idea is to make sure from node1, all its dest nodes and itself has no loop, then this node is safe
        # starting from each of the nodes, recursivly on it's dest nodes, until
        # 1. hit a node that has no dest nodes -> ok
        # 2. hit a node marked as "safe" -> ok
        # 3. hit a node we met previously but not marked as "safe", mean there's a loop - not Ok
        map2 = defaultdict(list)
        for dest, pre in prerequisites:
            map2[pre].append(dest)
        visited, ok_nodes = set(), set()

        def dfs(node):
            if node in visited:
                return False
            if node in ok_nodes:
                return True
            visited.add(node)
            ret = True
            for next in map2[node]:
                ret &= dfs(next)
            if ret:
                visited.remove(node)
                ok_nodes.add(node)
                return True
            else:
                return False

        ret = True
        for i in range(numCourses):
            ret &= dfs(i)
        return ret


# @lc code=end
