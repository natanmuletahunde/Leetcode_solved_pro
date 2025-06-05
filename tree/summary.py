class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(len(nums)):
            # Check if we're at the last number or the next number breaks the sequence
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i]}")
                if i < len(nums) - 1:
                    start = nums[i + 1]
        
        return result