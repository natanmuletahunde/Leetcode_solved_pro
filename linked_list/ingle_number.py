class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_all = 0
        for num in nums:
            xor_all ^= num  # XOR all numbers
        
        # Find the rightmost set bit (differentiating bit)
        diff_bit = xor_all & -xor_all 
        
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num  # XOR numbers in the first group
            else:
                num2 ^= num  # XOR numbers in the second group
        
        return [num1, num2]
