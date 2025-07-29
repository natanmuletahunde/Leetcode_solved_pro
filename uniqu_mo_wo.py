class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Morse code for a-z
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # Create a set to store unique transformations
        transformations = set()
        
        for word in words:
            # Transform the word into Morse code
            morse_word = ''.join(morse[ord(char) - ord('a')] for char in word)
            transformations.add(morse_word)
        
        # Return the number of unique Morse transformations
        return len(transformations)
