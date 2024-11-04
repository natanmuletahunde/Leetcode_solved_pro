# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and compare the values of each node
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the pointer to the next position in the merged list
            current = current.next

        # If there are remaining nodes in list1 or list2, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list, which starts after the dummy node
        return dummy.next
