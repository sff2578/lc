#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (55.27%)
# Likes:    4961
# Dislikes: 1367
# Total Accepted:    751K
# Total Submissions: 1.3M
# Testcase Example:  '00000010100101000001111010011100'
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
#
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 2 above, the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.
#
#
#
# Example 1:
#
#
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100
# represents the unsigned integer 43261596, so return 964176192 which its
# binary representation is 00111001011110000010100101000000.
#
#
# Example 2:
#
#
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101
# represents the unsigned integer 4294967293, so return 3221225471 which its
# binary representation is 10111111111111111111111111111111.
#
#
#
# Constraints:
#
#
# The input must be a binary string of length 32
#
#
#
# Follow up: If this function is called many times, how would you optimize it?
#
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            if n == 0:
                break
            cur = n % 2
            res += cur << i
            n = n // 2
        return res

    def reverseBits(self, n: int) -> int:
        r = 0
        for _ in range(32):
            r <<= 1
            r |= n & 1
            n >>= 1
        return r

    def reverseBits_1(self, n: int) -> int:
        res_ary = []
        while n > 0:
            res_ary.append(n % 2)
            n = n // 2
        res, start = 0, 32 - len(res_ary)
        for bit in res_ary[::-1]:
            res += bit << start
            start += 1
        return res


# @lc code=end
