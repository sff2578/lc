#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#
# https://leetcode.com/problems/snakes-and-ladders/description/
#
# algorithms
# Medium (44.68%)
# Likes:    2738
# Dislikes: 903
# Total Accepted:    167.8K
# Total Submissions: 381.7K
# Testcase Example:  '[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]'
#
# You are given an n x n integer matrix board where the cells are labeled from
# 1 to n^2 in a Boustrophedon style starting from the bottom left of the board
# (i.e. board[n - 1][0]) and alternating direction each row.
#
# You start on square 1 of the board. In each move, starting from square curr,
# do the following:
#
#
# Choose a destination square next with a label in the range [curr + 1,
# min(curr + 6, n^2)].
#
#
# This choice simulates the result of a standard 6-sided die roll: i.e., there
# are always at most 6 destinations, regardless of the size of the
# board.
#
#
# If next has a snake or ladder, you must move to the destination of that snake
# or ladder. Otherwise, you move to next.
# The game ends when you reach the square n^2.
#
#
# A board square on row r and column c has a snake or ladder if board[r][c] !=
# -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n^2
# do not have a snake or ladder.
#
# Note that you only take a snake or ladder at most once per move. If the
# destination to a snake or ladder is the start of another snake or ladder, you
# do not follow the subsequent snake or ladder.
#
#
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move,
# your destination square is 2. You follow the ladder to square 3, but do not
# follow the subsequent ladder to 4.
#
#
# Return the least number of moves required to reach the square n^2. If it is
# not possible to reach the square, return -1.
#
#
# Example 1:
#
#
# Input: board =
# [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so
# return 4.
#
#
# Example 2:
#
#
# Input: board = [[-1,-1],[-1,3]]
# Output: 1
#
#
#
# Constraints:
#
#
# n == board.length == board[i].length
# 2 <= n <= 20
# board[i][j] is either -1 or in the range [1, n^2].
# The squares labeled 1 and n^2 do not have any ladders or snakes.
#
#
#


# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # bfs
        # convert(): cell_idx -> cord
        # bfs: for each [cur+1, cur+7), record the step to reach here: step[cur]+1
        #   note: if this cord is seen before, do not update step, as it will definitly be bigger than current value
        #   note2: if there's a snake or ladder, directly go to the end, this is considered single transaction
        # until reach n*n, return the step
        n = len(board)

        def convert(num):
            div = num // n
            res = num % n
            r = n - div - 1
            c = 0
            if div % 2:
                # odd row from bottom, right-> left
                if res == 0:
                    r = n - div
                    c = n - 1
                else:
                    c = n - res
            else:
                # even row from bottom, left->right
                if res == 0:
                    r = n - div
                    c = 0
                else:
                    c = res - 1
            # print("num ", num, "r ", r, "c ", c)
            return r, c

        step = dict({1: 0})
        q = [1]
        while q:
            cur = q.pop(0)
            if cur == n * n:
                return step[cur]
            for next in range(cur + 1, cur + 7):
                if next > n * n:
                    continue
                r, c = convert(next)
                # print("next ", next, "r ", r, "c ", c)
                if board[r][c] != -1:
                    next = board[r][c]
                if next == n * n:
                    return step[cur] + 1
                if next not in step:
                    step[next] = step[cur] + 1
                    q.append(next)
            # print(q)
        return -1


# [[-1,-1,-1],[-1,9,8],[-1,8,9]]

# @lc code=end
