class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance_squared(pt1, pt2):
            """Calculate squared distance between two points."""
            return (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2
        
        # Get all pairwise distances
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distances.append(distance_squared(points[i], points[j]))
        
        # Sort distances
        distances.sort()
        
        # A valid square has:
        # - 4 equal sides (smallest 4 distances)
        # - 2 equal diagonals (largest 2 distances)
        # - The diagonals should be longer than the sides
        return (
            len(set(distances)) == 2 and  # Only two unique distances (sides and diagonals)
            distances.count(distances[0]) == 4 and  # 4 smallest distances are equal (sides)
            distances.count(distances[4]) == 2 and  # 2 largest distances are equal (diagonals)
            distances[0] > 0  # Positive side lengths
        )
