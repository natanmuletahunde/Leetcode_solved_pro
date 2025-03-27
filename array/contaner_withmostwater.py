class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1  # Two pointers at both ends
        max_water = 0  # Store maximum area

        while left < right:
            # Calculate the area
            h = min(height[left], height[right])  # Use the shorter height
            w = right - left  # Width is the distance between the two lines
            max_water = max(max_water, h * w)  # Update max area if larger
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
