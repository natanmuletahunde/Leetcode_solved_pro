class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math

        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-indexed
        result = ""

        for i in range(n, 0, -1):
            f = math.factorial(i - 1)
            index = k // f
            result += nums.pop(index)
            k %= f

        return result
