class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1)  # Add one extra 0 at the end for cleanup
        
        for row in matrix:
            for i in range(n_cols):
                # If the current value is '1', increase the height, else reset to 0
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Use stack to calculate max area in histogram
            stack = [-1]
            for i in range(n_cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area
