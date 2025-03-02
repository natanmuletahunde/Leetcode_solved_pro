class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4  # Assume 4 sides
                    
                    # Check adjacent cells and subtract for shared edges
                    if r > 0 and grid[r - 1][c] == 1:  # Check up
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:  # Check left
                        perimeter -= 2
        
        return perimeter
