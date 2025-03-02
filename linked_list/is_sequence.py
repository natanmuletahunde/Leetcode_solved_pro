class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize pointers for s and t
        i, j = 0, 0

        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer of s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer of t
            j += 1

        # If we traversed all of s, it is a subsequence
        return i == len(s)
