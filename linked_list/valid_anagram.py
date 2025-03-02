class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Anagrams must have the same length
        if len(s) != len(t):
            return False

        # Count the frequency of characters in both strings
        from collections import Counter
        return Counter(s) == Counter(t)

# Example Usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False
