from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        
        # Counters for unmatched characters in secret and guess
        secret_counter = Counter()
        guess_counter = Counter()
        
        # First pass: count bulls and track unmatched digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counter[s] += 1
                guess_counter[g] += 1
        
        # Second pass: count cows using the frequency counters
        for digit in guess_counter:
            if digit in secret_counter:
                cows += min(secret_counter[digit], guess_counter[digit])
        
        return "{}A{}B".format(bulls, cows)
