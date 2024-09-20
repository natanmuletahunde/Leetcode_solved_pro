/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);  // Dummy node to hold the result
    let current = dummy;          // Pointer to build the result linked list
    let carry = 0;                // Variable to store carry value during addition
    
    // Traverse both lists until both are exhausted
    while (l1 !== null || l2 !== null) {
        // Get the values from the current nodes of l1 and l2, if they exist
        let val1 = (l1 !== null) ? l1.val : 0;
        let val2 = (l2 !== null) ? l2.val : 0;
        
        // Calculate the sum of both values plus carry
        let sum = val1 + val2 + carry;
        
        // Update carry (if the sum is 10 or more, carry will be 1)
        carry = Math.floor(sum / 10);
        
        // Set the next node value to the remainder of sum divided by 10
        current.next = new ListNode(sum % 10);
        
        // Move the current pointer forward
        current = current.next;
        
        // Move l1 and l2 pointers forward, if they exist
        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }
    
    // If there's a carry left after the loop, add it as a new node
    if (carry > 0) {
        current.next = new ListNode(carry);
    }
    
    // Return the result linked list (dummy.next is the head of the result)
    return dummy.next;
};
