class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low=float('-inf'), high=float('inf')):
            # Base case: an empty node is valid
            if not node:
                return True
            
            # Check if the current node's value is out of the valid range
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)
