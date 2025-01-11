class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Create a prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Return the range sum using the prefix sum array
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Example Usage:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3
