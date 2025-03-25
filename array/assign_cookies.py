class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()  # Sort greed factors
        s.sort()  # Sort cookie sizes

        i, j = 0, 0  # Pointers for children and cookies
        count = 0  # Count of content children

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If the cookie can satisfy the child
                count += 1
                i += 1  # Move to next child
            j += 1  # Always move to next cookie

        return count  # Max number of content children
