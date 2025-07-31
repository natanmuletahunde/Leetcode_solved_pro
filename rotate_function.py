class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        
        max_f = f
        for i in range(1, n):
            f = f + total_sum - n * nums[-i]
            max_f = max(max_f, f)
        
        return max_f
