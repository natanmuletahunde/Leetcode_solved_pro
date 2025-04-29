class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Count frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Step 2: Find first character with count 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        return -1
