class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        
        # Count the frequency of each character in ransomNote and magazine
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Check if magazine has enough characters for ransomNote
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        
        return True
