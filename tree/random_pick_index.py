import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = None
        count = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # Reservoir Sampling: replace result with current index with probability 1/count
                if random.randint(1, count) == 1:
                    result = i
        return result
