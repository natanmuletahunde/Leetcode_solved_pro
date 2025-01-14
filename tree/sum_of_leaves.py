class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        def is_leaf(node):
            return node and not node.left and not node.right
        
        total = 0
        if is_leaf(root.left):  # Check if the left child is a leaf
            total += root.left.val
        
        # Recur for left and right subtrees
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total
