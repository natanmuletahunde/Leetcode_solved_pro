class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1         # digit length: 1-digit, 2-digit, ...
        count = 9          # count of numbers with that digit length
        start = 1          # starting number for this length

        # Step 1: Find the length of the number that contains the nth digit
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Find the actual number
        number = start + (n - 1) // length

        # Step 3: Find the digit in the number
        return int(str(number)[(n - 1) % length])
