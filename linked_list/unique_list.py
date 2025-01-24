class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        dummy = ListNode(0)  
        dummy.next = head
        prev = dummy
        
        
        for _ in range(left - 1):
            prev = prev.next
        
       
        current = prev.next
        next_node = None
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
