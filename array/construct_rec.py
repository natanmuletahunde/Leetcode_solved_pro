class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        
        width = int(math.sqrt(area))
        while area % width != 0:
            width -= 1
        
        length = area // width
        return [length, width]
