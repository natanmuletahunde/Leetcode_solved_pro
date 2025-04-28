class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2  # safer way to calculate mid to avoid overflow
            res = guess(mid)
            
            if res == 0:
                return mid  # Correct guess
            elif res == -1:
                right = mid - 1  # Guess is too high, search lower
            else:
                left = mid + 1  # Guess is too low, search higher
