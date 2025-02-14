class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))
        
        digit_map = defaultdict(list)
        max_sum = -1
        
        for num in nums:
            s = digit_sum(num)
            digit_map[s].append(num)
        
        for key in digit_map:
            digit_map[key].sort(reverse=True)
            if len(digit_map[key]) >= 2:
                max_sum = max(max_sum, digit_map[key][0] + digit_map[key][1])
        
        return max_sum