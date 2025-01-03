class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        def dfs(node, path, paths):
            if not node:
                return
            # Add the current node value to the path
            path += str(node.val)
            
            # If the node is a leaf, add the path to the paths list
            if not node.left and not node.right:
                paths.append(path)
            else:
                # Otherwise, continue to traverse the left and right subtrees
                path += "->"
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)
        
        paths = []
        dfs(root, "", paths)
        return paths
