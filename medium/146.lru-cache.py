#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (41.48%)
# Likes:    19915
# Dislikes: 929
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
#
#
#


# @lc code=start
class LRUCache:
    # map: key->node, node: pre, next, val
    # 2 way list, once use, move to end of list, keep head and tail of list
    def __init__(self, capacity: int):
        self.hash = dict()
        self.head = Node(0, 0, None, None)
        self.end = self.head
        self.cap = capacity
        self.print = False
        return

    def get(self, key: int) -> int:
        if self.print:
            print("before get", key)
            self.printInfo()
        if key not in self.hash.keys():
            return -1
        node = self.hash[key]
        # update node to last of list
        self.update(node)
        if self.print:
            print("after get")
            self.printInfo()
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.print:
            print("before put", key, value)
            self.printInfo()
        if key in self.hash.keys():
            node = self.hash[key]
            node.val = value
            self.update(node)
        else:
            if len(self.hash) == self.cap:
                # since cap >= 1, head.next can't be None
                del self.hash[self.head.next.key]
                self.head.next = self.head.next.next
                # head.next changed, may be none
                if self.head.next != None:
                    self.head.next.pre = self.head
                else:
                    self.end = self.head
            node = Node(key, value, self.end, None)
            self.hash[key] = node
            self.end.next = node
            self.end = node
        if self.print:
            print("after put")
            self.printInfo()

    # update list, move used to end of list
    def update(self, node):
        if self.print:
            print("updating node:", node.key, node)
        if self.end == node:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        self.end.next = node
        node.pre, node.next = self.end, None
        self.end = node

    def printInfo(self):
        print("end: ", self.end.key)
        cur = self.head
        print("list")
        while cur != None:
            print(" ", cur.key, "cur", cur, "prev", cur.pre, "next", cur.next)
            cur = cur.next
        print("map ", self.hash.keys())


class Node:
    def __init__(self, key, val, pre, next):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
