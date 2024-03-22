#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (50.27%)
# Likes:    33089
# Dislikes: 1390
# Total Accepted:    3.7M
# Total Submissions: 7.2M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curMax = nums[0], 0
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(curMax, maxSum)
        return maxSum

    def maxSubArray_2(self, nums: List[int]) -> int:
        # divid conquer, recursive on left_sub, cur_num, right_sub, max(left_sub, right_sub, cur_sub)
        # cur_sub will be starting from current, the max including left and right
        def recursive(left, right):
            if left > right:
                return -inf
            # max cur
            mid = (left + right) // 2
            cur_max = tmp_max = nums[mid]
            cnt = mid - 1
            while cnt >= left:
                tmp_max += nums[cnt]
                cur_max = max(cur_max, tmp_max)
                cnt -= 1
            cnt = mid + 1
            tmp_max = cur_max
            while cnt <= right:
                tmp_max += nums[cnt]
                cur_max = max(cur_max, tmp_max)
                cnt += 1
            # print("left ", left, "right ", right, "max", cur_max)
            return max(recursive(left, mid - 1), recursive(mid + 1, right), cur_max)

        return recursive(0, len(nums) - 1)

    def maxSubArray_1(self, nums: List[int]) -> int:
        # sliding window
        # total_max, cur_max, cur_sub_array_end
        m, cm, ce = nums[0], nums[0], 0
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur >= 0:
                # for positive numbers, alway use
                if i == ce + 1 and m >= 0:
                    # add to current subary
                    cm += cur
                else:
                    # sub ary broke, start a new one
                    cm = cur
                m = max(m, cm)
                ce = i
            else:
                # for negtivie numbers, depends on the sum
                if cur >= m:
                    m = cm = cur
                    ce = i
                elif i == ce + 1 and cm + cur >= 0:
                    cm += cur
                    ce = i
        return m


# @lc code=end
