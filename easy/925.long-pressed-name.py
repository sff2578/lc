#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (32.82%)
# Likes:    2265
# Dislikes: 324
# Total Accepted:    122.9K
# Total Submissions: 374.6K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard. Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard. Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed
# output.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
# @lc code=end

