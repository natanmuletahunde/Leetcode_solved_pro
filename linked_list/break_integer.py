class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2

        # The optimal strategy is to break n into as many 3s as possible.
        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            # If remainder is 1, it's better to take one '3' and turn it into two '2's (3 + 1 = 2 + 2).
            return 3 ** (quotient - 1) * 4
        else:
            # If remainder is 2, multiply by it directly
            return 3 ** quotient * 2
