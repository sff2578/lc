#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (42.56%)
# Likes:    6058
# Dislikes: 449
# Total Accepted:    429.8K
# Total Submissions: 999.9K
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#
#
# Example 1:
#
#
# Input: s = "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
#
# Example 3:
#
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is
# invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is
# valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.
#
#
#


# @lc code=start
class Solution:
    def updateStack(self, num, operator, stack):
        # operator is previous operator, number is pervious number
        if operator == "+":
            stack.append(num)
        elif operator == "-":
            stack.append(-num)
        # let not consider */ yet

    def calculate(self, s: str) -> int:
        # loop through, if meet an operator, calculate the previous number and operator in stack
        # start with operator +
        # if previous operator is +, add the previous number to stack, if *or/, pop stack and *or/ with previous number
        # if meet (, treat this as a number, but before that, recursivly call self.calculate to get the number between (). if meet ), this calculate is done, return
        ret, j = self.calculate_helper(s)
        return ret

    def calculate_helper(self, s: str):
        # loop through, if meet an operator, calculate the previous number and operator in stack
        # start with operator +
        # if previous operator is +, add the previous number to stack, if *or/, pop stack and *or/ with previous number
        # if meet (, treat this as a number, but before that, recursivly call self.calculate to get the number between (). if meet ), this calculate is done, return
        operator, num, stack, it = "+", 0, [], 0
        # print("checking string ", s)
        while it < len(s):
            char = s[it]
            if char.isdigit():
                # first get the number(may have multple digits), and move it to the last digit
                num, ctr = char, it + 1
                while ctr < len(s):
                    if s[ctr].isdigit():
                        num += s[ctr]
                        ctr += 1
                    else:
                        break
                it = ctr - 1
                # print("num string", num)
                num = int(num)
                # print("num int", num)
            elif char in "+-":
                self.updateStack(num, operator, stack)
                operator = char
            elif char == "(":
                # treat as a number
                num, j = self.calculate_helper(s[it + 1 :])
                # print("() number", num)
                # update it to the ending )
                it += j
                # print("cur it", it)
            elif char == ")":
                self.updateStack(num, operator, stack)
                return sum(stack), it + 1
            it += 1
        self.updateStack(num, operator, stack)
        return sum(stack), it - 1


# "(1+(4+5+2)-3)+(6+8)"
# "0123456789"
# cal0
# num 0 9 14 opr + stack[9 14] = 23
# cal1
# num 1 11 3 opr + - stack[1 11 -3] ->9
# cal2
# num 4 5 2 opr + + + stack[4 5 2] ->11
# cal3
# num 0 6 8 opr + + stack[6 8]->14

# "2147483647"
# @lc code=end
