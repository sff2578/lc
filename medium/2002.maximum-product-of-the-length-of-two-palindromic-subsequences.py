#
# @lc app=leetcode id=2002 lang=python3
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/
#
# algorithms
# Medium (55.70%)
# Likes:    817
# Dislikes: 57
# Total Accepted:    21.4K
# Total Submissions: 38K
# Testcase Example:  '"leetcodecom"'
#
# Given a string s, find two disjoint palindromic subsequences of s such that
# the product of their lengths is maximized. The two subsequences are disjoint
# if they do not both pick a character at the same index.
# 
# Return the maximum possible product of the lengths of the two palindromic
# subsequences.
# 
# A subsequence is a string that can be derived from another string by deleting
# some or no characters without changing the order of the remaining characters.
# A string is palindromic if it reads the same forward and backward.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1^st subsequence
# and "cdc" for the 2^nd subsequence.
# The product of their lengths is: 3 * 3 = 9.
# 
# 
# Example 2:
# 
# 
# Input: s = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) for
# the 1^st subsequence and "b" (the second character) for the 2^nd subsequence.
# The product of their lengths is: 1 * 1 = 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1^st
# subsequence and "xxcxx" for the 2^nd subsequence.
# The product of their lengths is: 5 * 5 = 25.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 12
# s consists of lowercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        
        Intuition:

#Idea is to form all combinations of subsequences that are palindromic, that are not overlapping i.e first string and second string should not have any common element from main string. Out of all possible first and second strings, we find product of first.size() * second.size() . In the end we return the maximum product.
#
#Next, looking at the size of given string i.e 1 <= n <= 12. We can do a brute force over it and use Backtracking to get all possible combinations of first and second string that are subsequences of original string.
#
#Now, lets see how can we form first and second string? Think of possible choices at every index of the original string. What can we pick and what we can skip. Since, we are given that both the palindromic should not have any common element (non-overlapping and disjoint). Thus, we cannot include current element in both strings simultaneously.
#
#So, we have actually 3 choices at every index.
#
#Exclude the current element from both first and second string.
#
#Include the current element into first string -> Backtracking, include -> use -> remove
#
#Include the current element into second string. -> Backtracking, include -> use -> remove
#
#Base Condition : : When we reach the end of string, check if first and second string are palindrome or not.
#
#If not then return
#Else calculate the product of lengths first.size() * second.size() and update maximumProduct accordingly
#Go through the code, it is self explainatory and easy to understand. Just simple backtracking logic, nothing complex.
#
#Note: We are passing first and second strings by reference, so that in every function call new copies of string is not created. If we do not consider this, it will give a TLE.
# @lc code=end

#class Solution {
#public:
#    int result = 0;
#    bool isPalin(string& s){
#        int i = 0;
#        int j = s.length() - 1;
# 
#        while (i < j) {
#            if (s[i] != s[j]) return false;
#            i++;
#            j--;
#        }
# 
#        return true;
#    }
#    
#    void dfs(string& s, int i, string& s1, string& s2){
#        
#        if(i >= s.length()){
#            if(isPalin(s1) && isPalin(s2))
#                result = max(result, (int)s1.length()*(int)s2.length());
#            return;
#        }
#        
#        s1.push_back(s[i]);
#        dfs(s, i+1, s1, s2);
#        s1.pop_back();
#        
#        s2.push_back(s[i]);
#        dfs(s, i+1, s1, s2);
#        s2.pop_back();
#        
#        dfs(s, i+1, s1, s2);
#    }
#    
#    int maxProduct(string s) {
#        string s1 = "", s2 = "";
#        dfs(s, 0, s1, s2);
#        
#        return result;
#    }
#};