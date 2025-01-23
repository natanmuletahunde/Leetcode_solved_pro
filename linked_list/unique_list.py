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
        
        dummy = ListNode(0)  # Create a dummy node to simplify edge cases
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the sublist from left to right
        current = prev.next
        next_node = None
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
