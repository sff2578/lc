#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (38.14%)
# Likes:    2499
# Dislikes: 3620
# Total Accepted:    307.5K
# Total Submissions: 801.7K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of strings words and a width maxWidth, format the text such
# that each line has exactly maxWidth characters and is fully (left and right)
# justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line does not divide evenly between words, the
# empty slots on the left will be assigned more spaces than the slots on the
# right.
#
# For the last line of text, it should be left-justified, and no extra space is
# inserted between words.
#
# Note:
#
#
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
#
#
#
# Example 1:
#
#
# Input: words = ["This", "is", "an", "example", "of", "text",
# "justification."], maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
# Example 2:
#
#
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
# 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one
# word.
#
# Example 3:
#
#
# Input: words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
# Constraints:
#
#
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
#
#
#


# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        # curLen total length of all words only(no pace), curCnt total count of words
        curLen = curCnt = 0
        curList = []
        totalList = []
        eachLen = []
        for i in range(len(words)):
            thisLen = len(words[i])
            # adding curCnt to make sure at least on space between words
            totalLen = curLen + thisLen + curCnt
            if totalLen <= maxWidth:
                # if adding this word still not exceed maxWidth, add this to current list
                # note how many words in current list
                curLen += thisLen
                curCnt += 1
                curList.append(words[i])
            else:
                # if exceeding maxWidth, finished one line, start a new line with this word
                totalList.append(curList)
                eachLen.append(curLen)
                curList = [words[i]]
                curCnt = 1
                curLen = thisLen
        # in case of not reaching maxWidth, don't miss the last few words
        if curLen > 0:
            totalList.append(curList)
            eachLen.append(curLen)
        for i in range(len(totalList) - 1):
            if len(totalList[i]) == 1:
                evenSpaces = 0
                extraSpaces = maxWidth - len(totalList[i][0])
            else:
                evenSpaces = (maxWidth - eachLen[i]) // (len(totalList[i]) - 1)
                extraSpaces = (maxWidth - eachLen[i]) % (len(totalList[i]) - 1)
            curStr = ""
            for j in range(len(totalList[i])):
                if j < len(totalList[i]) - 1:
                    curStr += totalList[i][j] + " " * evenSpaces
                    if extraSpaces > 0:
                        curStr += " "
                        extraSpaces -= 1
                else:
                    strLen = len(curStr) + len(totalList[i][j])
                    rem = maxWidth - strLen
                    curStr += totalList[i][j] + " " * rem
            ret.append(curStr)
        # last entry abc abc  , 9
        length = 0
        curStr = ""
        for j in range(len(totalList[-1])):
            if j < len(totalList[-1]) - 1:
                curStr += totalList[-1][j] + " "
                length += len(totalList[-1][j]) + 1
            else:
                curStr += totalList[-1][j] + " " * (
                    maxWidth - length - len(totalList[-1][j])
                )

        ret.append(curStr)
        return ret

    def fullJustify_2(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [" ".join(cur).ljust(maxWidth)]


# @lc code=end
