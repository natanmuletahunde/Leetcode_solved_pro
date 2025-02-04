class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        if len(pattern) != len(words):  
            return False
        
        char_to_word = {}  # Dictionary to map pattern characters to words
        word_to_char = {}  
        
        for char, word in zip(pattern, words):  # Iterate through both together
            if char in char_to_word:  # Check if char is already mapped
                if char_to_word[char] != word: 
                    return False
            else:
                if word in word_to_char: 
                    return False
                char_to_word[char] = word
                word_to_char[word] = char
        
        return True  
