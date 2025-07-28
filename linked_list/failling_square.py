class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        result = []
        squares = []  # stores (start, end, height)
        max_height = 0
        
        for left, size in positions:
            right = left + size
            base_height = 0
            
            for l, r, h in squares:
                if right > l and left < r:  # Overlapping condition
                    base_height = max(base_height, h)
            
            new_height = base_height + size
            squares.append((left, right, new_height))
            max_height = max(max_height, new_height)
            result.append(max_height)
        
        return result
