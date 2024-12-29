class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def getDepth(node):
            """
            Helper function to calculate the depth of the tree.
            """
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        if not root:
            return 0
        
        # Get the depth of the leftmost and rightmost paths
        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)

        if left_depth == right_depth:
            # Left subtree is a perfect binary tree
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree
            return (1 << right_depth) + self.countNodes(root.left)
