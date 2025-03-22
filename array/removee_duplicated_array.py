# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that helps to handle edge cases (e.g. head is duplicate)
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' is the last node before the sublist of duplicates
        prev = dummy
        
        while head:
            # If current node has a duplicate...
            if head.next and head.val == head.next.val:
                # Skip nodes until the value changes
                duplicate_val = head.val
                while head and head.val == duplicate_val:
                    head = head.next
                # Link prev node to the first node with a new value (could be None)
                prev.next = head
            else:
                # No duplicate for current node, move prev pointer forward
                prev = prev.next
                head = head.next
                
        return dummy.next
