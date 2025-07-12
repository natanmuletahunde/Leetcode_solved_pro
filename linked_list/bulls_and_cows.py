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

        # Counters for non-bull characters
        secret_counter = Counter()
        guess_counter = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counter[s] += 1
                guess_counter[g] += 1

        # Count cows by taking the min count of common digits in secret and guess
        for digit in guess_counter:
            cows += min(secret_counter[digit], guess_counter[digit])

        return f"{bulls}A{cows}B"
