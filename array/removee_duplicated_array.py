class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  # Connect to non-duplicate node
            else:
                prev = prev.next  # Move forward only if no duplicates
            head = head.next  # Continue traversal
        
        return dummy.next
