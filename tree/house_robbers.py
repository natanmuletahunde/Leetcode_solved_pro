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
        
        prev1 = 0 
        prev2 = 0
        
        for num in nums:
            temp = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = temp
            
        return prev2
