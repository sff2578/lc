#
# @lc app=leetcode id=1702 lang=python3
#
# [1702] Maximum Binary String After Change
#
# https://leetcode.com/problems/maximum-binary-string-after-change/description/
#
# algorithms
# Medium (46.64%)
# Likes:    483
# Dislikes: 51
# Total Accepted:    12.5K
# Total Submissions: 26.7K
# Testcase Example:  '"000110"'
#
# You are given a binary string binary consisting of only 0's or 1's. You can
# apply each of the following operations any number of times:
# 
# 
# Operation 1: If the number contains the substring "00", you can replace it
# with "10".
# 
# 
# For example, "00010" -> "10010"
# 
# 
# Operation 2: If the number contains the substring "10", you can replace it
# with "01".
# 
# For example, "00010" -> "00001"
# 
# 
# 
# 
# Return the maximum binary string you can obtain after any number of
# operations. Binary string x is greater than binary string y if x's decimal
# representation is greater than y's decimal representation.
# 
# 
# Example 1:
# 
# 
# Input: binary = "000110"
# Output: "111011"
# Explanation: A valid transformation sequence can be:
# "000110" -> "000101" 
# "000101" -> "100101" 
# "100101" -> "110101" 
# "110101" -> "110011" 
# "110011" -> "111011"
# 
# 
# Example 2:
# 
# 
# Input: binary = "01"
# Output: "01"
# Explanation: "01" cannot be transformed any further.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= binary.length <= 10^5
# binary consist of '0' and '1'.
# 
# 
#

# @lc code=start
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        
# @lc code=end

