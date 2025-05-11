class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize two variables to store max amounts
        prev1 = 0  # max amount till the house before previous
        prev2 = 0  # max amount till previous house
        
        for num in nums:
            temp = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = temp
            
        return prev2
