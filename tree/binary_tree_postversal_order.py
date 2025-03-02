class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)   # Traverse the left subtree
            dfs(node.right)  # Traverse the right subtree
            result.append(node.val)  # Visit the root node

        dfs(root)
        return result
