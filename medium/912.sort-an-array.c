/*
 * @lc app=leetcode id=912 lang=c
 *
 * [912] Sort an Array
 *
 * https://leetcode.com/problems/sort-an-array/description/
 *
 * algorithms
 * Medium (56.86%)
 * Likes:    5887
 * Dislikes: 738
 * Total Accepted:    583.2K
 * Total Submissions: 1M
 * Testcase Example:  '[5,2,3,1]'
 *
 * Given an array of integers nums, sort the array in ascending order and
 * return it.
 * 
 * You must solve the problem without using any built-in functions in
 * O(nlog(n)) time complexity and with the smallest space complexity
 * possible.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [5,2,3,1]
 * Output: [1,2,3,5]
 * Explanation: After sorting the array, the positions of some numbers are not
 * changed (for example, 2 and 3), while the positions of other numbers are
 * changed (for example, 1 and 5).
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [5,1,1,2,0,0]
 * Output: [0,0,1,1,2,5]
 * Explanation: Note that the values of nums are not necessairly unique.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 5 * 10^4
 * -5 * 10^4 <= nums[i] <= 5 * 10^4
 * 
 * 
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {
   int *new_nums =  (int *)malloc(numsSize * sizeof(int));
   memcpy(new_nums, nums, numsSize*sizeof(int));
   *returnSize = numsSize;
   //quickSory(new_nums, 0, numsSize-1);
   quicksort(new_nums, 0, numsSize-1);
   return new_nums;
}

void quickSory(int* nums, int s, int e) {
    if (s >= e) {
        return;
    }
    int i = s, j = e, pivot = nums[s];
    while(i <= j) {
        while(i <= j && nums[i] < pivot) {
            i++;
        }
        while(i <= j && nums[j] > pivot) {
            j--;
        }
        if (i <= j) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
            j--;
        }
    }
    quickSory(nums, s, j);
    quickSory(nums, i, e);
    return;
}

void quicksort(int*nums, int s, int e) {
    // 04/05/2024 quick sort
    if (s > e) {
        return;
    }
    int pivot = nums[s];
    int i = s+1, j = e; 
    while (i <= j) {
        while(i <= j && nums[i] < pivot) {
            i++;
        }
        while(i <= j && nums[j] > pivot) {
            j--;
        }
        if (i <= j) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
            j--;
        }
    }
    int tmp = nums[j];
    nums[j] = nums[s];
    nums[s] = tmp;
    quicksort(nums, s, j-1);
    quicksort(nums, i, e);
    return;
}
// @lc code=end

