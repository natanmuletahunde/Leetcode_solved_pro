class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # Base case: if the list is empty or has a single node, it's already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Divide the list into two halves
        def split(head):
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            mid = slow.next
            slow.next = None
            return head, mid
        
        # Step 2: Merge the two sorted halves
        def merge(l1, l2):
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2
            return dummy.next
        
        # Split the list into two halves
        left, right = split(head)
        
        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted halves
        return merge(left, right)
