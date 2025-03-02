class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        dp = [False] * (len(s) + 1)  # Initialize dp array
        dp[0] = True  # Base case: empty string can be segmented
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if we found a valid segmentation
        
        return dp[len(s)]  # Return whether the whole string can be segmented