#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (41.08%)
# Likes:    16605
# Dislikes: 680
# Total Accepted:    1.1M
# Total Submissions: 2.8M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
#
# Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
# Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
# Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
# Constraints:
#
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#
#


# Input: s = "ADOBECODEBANC", t = "ABC"
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # map t to A:1 B:1 C:1
        # before all t char got, fast++, remember the substring, after all t got, slow++ until t not met, then fast++
        map_of_t = self.tToMap(t)
        count, min_len = len(map_of_t), 10**5
        slow = fast = 0
        res = s
        found = False
        while fast < len(s):
            c_char = s[fast]
            if c_char in map_of_t.keys():
                c_cnt = map_of_t[c_char] - 1
                map_of_t[c_char] = c_cnt
                if c_cnt == 0:
                    count -= 1
            while count == 0:
                found = True
                cur_substr = s[slow : fast + 1]
                if len(res) > len(cur_substr):
                    res = cur_substr
                s_char = s[slow]
                if s_char in map_of_t.keys():
                    s_cnt = map_of_t[s_char] + 1
                    map_of_t[s_char] = s_cnt
                    if s_cnt > 0:
                        count += 1
                slow += 1
            fast += 1
        if found:
            return res
        else:
            return ""

    def tToMap(self, t):
        map_of_t = dict()
        for i in range(len(t)):
            cnt = map_of_t.get(t[i], 0) + 1
            map_of_t[t[i]] = cnt
        return map_of_t


# @lc code=end
#
# string minWindow(string s, string t) {
#        vector<int> map(128,0);
#        for(auto c: t) map[c]++;
#        int counter=t.size(), begin=0, end=0, d=INT_MAX, head=0;
#        while(end<s.size()){
#            if(map[s[end++]]-->0) counter--; //in t
#            while(counter==0){ //valid
#                if(end-begin<d)  d=end-(head=begin);
#                if(map[s[begin++]]++==0) counter++;  //make it invalid
#            }
#        }
#        return d==INT_MAX? "":s.substr(head, d);
#    }
# Here comes the template.
#
# For most substring problem, we are given a string and need to find a substring of it which satisfy some restrictions. A general way is to use a hashmap assisted with two pointers. The template is given below.
#
# int findSubstring(string s){
#        vector<int> map(128,0);
#        int counter; // check whether the substring is valid
#        int begin=0, end=0; //two pointers, one point to tail and one  head
#        int d; //the length of substring
#
#        for() { /* initialize the hash map here */ }
#
#        while(end<s.size()){
#
#            if(map[s[end++]]-- ?){  /* modify counter here */ }
#
#            while(/* counter condition */){
#
#                 /* update d here if finding minimum*/
#
#                //increase begin to make it invalid/valid again
#
#                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
#            }
#
#            /* update d here if finding maximum*/
#        }
#        return d;
#  }
# One thing needs to be mentioned is that when asked to find maximum substring, we should update maximum after the inner while loop to guarantee that the substring is valid. On the other hand, when asked to find minimum substring, we should update minimum inside the inner while loop.
#
# The code of solving Longest Substring with At Most Two Distinct Characters is below:
#
# int lengthOfLongestSubstringTwoDistinct(string s) {
#        vector<int> map(128, 0);
#        int counter=0, begin=0, end=0, d=0;
#        while(end<s.size()){
#            if(map[s[end++]]++==0) counter++;
#            while(counter>2) if(map[s[begin++]]--==1) counter--;
#            d=max(d, end-begin);
#        }
#        return d;
#    }
# The code of solving Longest Substring Without Repeating Characters is below:
#
# Update 01.04.2016, thanks @weiyi3 for advise.
#
# int lengthOfLongestSubstring(string s) {
#        vector<int> map(128,0);
#        int counter=0, begin=0, end=0, d=0;
#        while(end<s.size()){
#            if(map[s[end++]]++>0) counter++;
#            while(counter>0) if(map[s[begin++]]-->1) counter--;
#            d=max(d, end-begin); //while valid, update d
#        }
#        return d;
#    }
# I think this post deserves some upvotes! : )
