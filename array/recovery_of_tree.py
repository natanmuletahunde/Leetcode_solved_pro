# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None. Modify root in-place.
        """
        first = second = prev = None
        current = root

        while current:
            if current.left is None:
                # Visit node
                if prev and current.val < prev.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                # Find the inorder predecessor
                pred = current.left
                while pred.right and pred.right != current:
                    pred = pred.right

                if pred.right is None:
                    pred.right = current
                    current = current.left
                else:
                    pred.right = None
                    if prev and current.val < prev.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right

        # Swap the values of the two incorrect nodes
        if first and second:
            first.val, second.val = second.val, first.val
