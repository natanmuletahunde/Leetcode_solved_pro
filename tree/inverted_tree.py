from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Edge case: if the tree is empty
        if not root:
            return None

        # Initialize a queue for BFS
        queue = deque([root])

        while queue:
            # Get the current node
            current = queue.popleft()

            # Swap its left and right children
            current.left, current.right = current.right, current.left

            # Add the children to the queue if they exist
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root
