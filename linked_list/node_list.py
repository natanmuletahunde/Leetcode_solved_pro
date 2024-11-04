# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Traverse the list in pairs
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Perform the swap
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move to the next pair
            prev = first
            
        # Return the new head (which is next of dummy)
        return dummy.next
