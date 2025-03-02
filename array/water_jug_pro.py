class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        from math import gcd
        # If target is greater than the combined capacity, it's impossible
        if target > x + y:
            return False
        # The target must be a multiple of the GCD of x and y
        return target % gcd(x, y) == 0
