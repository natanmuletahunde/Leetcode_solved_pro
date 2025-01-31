class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()  # Split the string into words
        
        if len(pattern) != len(words):  # If lengths don't match, return False
            return False
        
        char_to_word = {}  # Dictionary to map pattern characters to words
        word_to_char = {}  # Dictionary to map words to pattern characters
        
        for char, word in zip(pattern, words):  # Iterate through both together
            if char in char_to_word:  # Check if char is already mapped
                if char_to_word[char] != word:  # If it maps to a different word, return False
                    return False
            else:
                if word in word_to_char:  # If word is already mapped to another char, return False
                    return False
                char_to_word[char] = word
                word_to_char[word] = char
        
        return True  # If no mismatches found, return True
