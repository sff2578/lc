/*
 * @lc app=leetcode id=287 lang=c
 *
 * [287] Find the Duplicate Number
 *
 * https://leetcode.com/problems/find-the-duplicate-number/description/
 *
 * algorithms
 * Medium (59.45%)
 * Likes:    22934
 * Dislikes: 4346
 * Total Accepted:    1.7M
 * Total Submissions: 2.8M
 * Testcase Example:  '[1,3,4,2,2]'
 *
 * Given an array of integers nums containing n + 1 integers where each integer
 * is in the range [1, n] inclusive.
 * 
 * There is only one repeated number in nums, return this repeated number.
 * 
 * You must solve the problem without modifying the array nums and uses only
 * constant extra space.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,3,4,2,2]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,1,3,4,2]
 * Output: 3
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [3,3,3,3,3]
 * Output: 3
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10^5
 * nums.length == n + 1
 * 1 <= nums[i] <= n
 * All the integers in nums appear only once except for precisely one integer
 * which appears two or more times.
 * 
 * 
 * 
 * Follow up:
 * 
 * 
 * How can we prove that at least one duplicate number must exist in nums?
 * Can you solve the problem in linear runtime complexity?
 * 
 * 
 */

// @lc code=start
int findDuplicate(int* nums, int numsSize) {
   // 04/04/2024 
   // linked list cycle
   int fast = nums[0], slow = nums[0];
   while (true) {
        fast = nums[nums[fast]];
        slow = nums[slow];
        if (fast == slow) {
            break;
        }
   }
   fast = nums[0];
   while(fast != slow) {
    fast = nums[fast];
    slow = nums[slow];
   }
   return fast;
}
// @lc code=end

