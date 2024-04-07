/*
 * @lc app=leetcode id=234 lang=c
 *
 * [234] Palindrome Linked List
 *
 * https://leetcode.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (51.80%)
 * Likes:    16213
 * Dislikes: 868
 * Total Accepted:    1.9M
 * Total Submissions: 3.5M
 * Testcase Example:  '[1,2,2,1]'
 *
 * Given the head of a singly linked list, return true if it is a palindrome or
 * false otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: head = [1,2,2,1]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: head = [1,2]
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the list is in the range [1, 10^5].
 * 0 <= Node.val <= 9
 * 
 * 
 * 
 * Follow up: Could you do it in O(n) time and O(1) space?
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    // reverse half of the list
    struct ListNode *prev = NULL;
    struct ListNode *slow = head, *fast = head, *cur = head;
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;
        cur->next = prev;
        prev = cur;
        cur = slow;
    }
    if (fast != NULL) {
        slow = slow->next;
    }
    while(slow != NULL && prev != NULL) {
        if (slow->val != prev->val) {
            return false;
        }
        slow = slow->next;
        prev = prev->next;
    }
    return true;
}
// @lc code=end

