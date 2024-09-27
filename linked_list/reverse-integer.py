class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle the sign of the number
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits of the number
        reversed_x = 0
        while x != 0:
            pop = x % 10  # Get the last digit
            x //= 10  # Remove the last digit
            # Check if the reversed number will overflow
            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and pop > 7):
                return 0
            reversed_x = reversed_x * 10 + pop
        
        # Return the result with the correct sign
        return sign * reversed_x