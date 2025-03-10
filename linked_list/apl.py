class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # Sort the input to ensure that every later number is larger than previous ones.
        nums.sort()
        
        # dp[i] will hold the largest divisible subset ending with nums[i]
        dp = [[] for _ in range(len(nums))]
        
        for i, num in enumerate(nums):
            # Start with an empty subset for comparison.
            max_subset = []
            # Check all numbers before nums[i]
            for j in range(i):
                # If the current number is divisible by nums[j] and dp[j] is the largest found so far
                if num % nums[j] == 0 and len(dp[j]) > len(max_subset):
                    max_subset = dp[j]
            # Append current number to the best subset found ending with a divisor of num
            dp[i] = max_subset + [num]
        
        # Return the subset with maximum length among all dp entries.
        return max(dp, key=len)
