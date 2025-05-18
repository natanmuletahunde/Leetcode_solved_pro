class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def dfs(r, c):
            # If out of bounds or water, return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Mark this cell as visited
            grid[r][c] = '0'
            # Explore all adjacent cells (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1  # One full island explored
        
        return count
