from collections import deque, defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        # If there is only one node, the answer is trivially that node
        if n == 1:
            return [0]
        
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Initialize the leaves
        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:  # If the node has only one neighbor, it is a leaf
                leaves.append(i)
        
        # Step 3: Trim the leaves until we have 1 or 2 nodes remaining
        while n > 2:
            # Remove the current leaves
            n -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                # Remove the leaf from its neighbor
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                # If the neighbor becomes a leaf, add it to the leaves queue
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
        
        # Step 4: The remaining nodes are the roots of the MHTs
        return list(leaves)
