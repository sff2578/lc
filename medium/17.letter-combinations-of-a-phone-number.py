#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (57.38%)
# Likes:    17880
# Dislikes: 951
# Total Accepted:    1.9M
# Total Submissions: 3.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letter_ary = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if len(digits) == 0:
            return res
        dfs_ret = self.letterCombinations(digits[1:])
        cur_digit = int(digits[0])
        for char in letter_ary[cur_digit]:
            if len(dfs_ret) == 0:
                res.append(char)
            else:
                for str in dfs_ret:
                    res.append(char + str)
        return res


# @lc code=end
