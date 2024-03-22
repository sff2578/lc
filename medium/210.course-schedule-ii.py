#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (49.01%)
# Likes:    10392
# Dislikes: 330
# Total Accepted:    956.3K
# Total Submissions: 1.9M
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
#
#
# Example 2:
#
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
#
#
# Example 3:
#
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
#
#
#


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.findOrder_dfs(numCourses, prerequisites)

    def findOrder_khan(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
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

        reached_lsit, ret_list = [], []
        for node in range(numCourses):
            pre_list = map1[node]
            if not pre_list:
                del map1[node]
                reached_lsit.append(node)
        while reached_lsit:
            cur = reached_lsit.pop(0)
            ret_list.append(cur)
            for dest in map2[cur]:
                map1[dest].remove(cur)
                if not map1[dest]:
                    reached_lsit.append(dest)
                    del map1[dest]
        if len(map1) == 0:
            return ret_list
        else:
            return []

    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        ret_l = []

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
                ret_l.insert(0, node)
                return True
            else:
                return False

        ret = True
        for i in range(numCourses):
            ret &= dfs(i)
        if ret:
            return ret_l
        else:
            return []


# @lc code=end
