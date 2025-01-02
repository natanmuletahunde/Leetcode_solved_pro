class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize pointers for binary search
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2  # Calculate mid to avoid overflow
            if isBadVersion(mid):
                # If mid is a bad version, search the left half
                right = mid
            else:
                # If mid is not a bad version, search the right half
                left = mid + 1
        
        # When left == right, it points to the first bad version
        return left
