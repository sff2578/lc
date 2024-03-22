#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#
# https://leetcode.com/problems/design-front-middle-back-queue/description/
#
# algorithms
# Medium (56.63%)
# Likes:    725
# Dislikes: 103
# Total Accepted:    26K
# Total Submissions: 46K
# Testcase Example:  '["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]\n' +
#'[[],[1],[2],[3],[4],[],[],[],[],[]]'
#
# Design a queue that supports push and pop operations in the front, middle,
# and back.
#
# Implement the FrontMiddleBack class:
#
#
# FrontMiddleBack() Initializes the queue.
# void pushFront(int val) Adds val to the front of the queue.
# void pushMiddle(int val) Adds val to the middle of the queue.
# void pushBack(int val) Adds val to the back of the queue.
# int popFront() Removes the front element of the queue and returns it. If the
# queue is empty, return -1.
# int popMiddle() Removes the middle element of the queue and returns it. If
# the queue is empty, return -1.
# int popBack() Removes the back element of the queue and returns it. If the
# queue is empty, return -1.
#
#
# Notice that when there are two middle position choices, the operation is
# performed on the frontmost middle position choice. For example:
#
#
# Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4,
# 5].
# Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4,
# 5, 6].
#
#
#
# Example 1:
#
#
# Input:
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle",
# "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# Output:
# [null, null, null, null, null, 1, 3, 4, 2, -1]
#
# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (The queue is empty)
#
#
#
# Constraints:
#
#
# 1 <= val <= 10^9
# At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront,
# popMiddle, and popBack.
#
#
#


# @lc code=start
class FrontMiddleBackQueue:
    # 2 deque, keep front <= back, when add middle, add to back of front and re-balance

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())

    def pushMiddle(self, val: int) -> None:
        self.front.append(val)
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        if len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())

    def popFront(self) -> int:
        if len(self.back) > len(self.front):
            self.front.append(self.back.popleft())
        return self.front.popleft() if len(self.front) > 0 else -1

    def popMiddle(self) -> int:
        if len(self.back) == len(self.front):
            if len(self.front) == 0:
                return -1
            self.back.appendleft(self.front.pop())
        return self.back.popleft()

    def popBack(self) -> int:
        if len(self.back) == len(self.front):
            if len(self.front) == 0:
                return -1
            self.back.appendleft(self.front.pop())
        return self.back.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end
