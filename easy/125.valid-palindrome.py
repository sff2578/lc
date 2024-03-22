#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (45.14%)
# Likes:    8031
# Dislikes: 7768
# Total Accepted:    2.2M
# Total Submissions: 4.9M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            # print("i %s j %s" % (s[i], s[j]))
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            elif not s[i].isalnum():
                i += 1
            else:
                j -= 1
        return True


# @lc code=end
