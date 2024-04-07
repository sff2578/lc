/*
 * @lc app=leetcode id=328 lang=c
 *
 * [328] Odd Even Linked List
 *
 * https://leetcode.com/problems/odd-even-linked-list/description/
 *
 * algorithms
 * Medium (61.38%)
 * Likes:    9723
 * Dislikes: 515
 * Total Accepted:    895.2K
 * Total Submissions: 1.5M
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * Given the head of a singly linked list, group all the nodes with odd indices
 * together followed by the nodes with even indices, and return the reordered
 * list.
 * 
 * The first node is considered odd, and the second node is even, and so on.
 * 
 * Note that the relative order inside both the even and odd groups should
 * remain as it was in the input.
 * 
 * You must solve the problem in O(1) extra space complexity and O(n) time
 * complexity.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: head = [1,2,3,4,5]
 * Output: [1,3,5,2,4]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: head = [2,1,3,5,6,4,7]
 * Output: [2,3,6,7,1,5,4]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the linked list is in the range [0, 10^4].
 * -10^6 <= Node.val <= 10^6
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    struct ListNode *oddH=NULL, *evenH=NULL;    
    struct ListNode *oddT=NULL, *evenT=NULL;    
    struct ListNode *cur = head;
    int count = 1;
    while (cur != NULL) {
        if (count % 2 == 1) {
            // odd
            if (oddH == NULL) {
                oddH = cur;
            } else {
                oddT->next = cur;
            }
            oddT = cur;
        } else {
            // even
            if (evenH == NULL) {
                evenH = cur;
            } else {
                evenT->next = cur;
            }
            evenT = cur;
        }
        cur = cur->next;
        count++;
    }
    if (oddT != NULL) {
        oddT->next = evenH;
    }
    if (evenT != NULL) {
        evenT->next = NULL;
    }
    return oddH;
}
// @lc code=end

