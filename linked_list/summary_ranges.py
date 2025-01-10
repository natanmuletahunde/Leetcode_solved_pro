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
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        
        # Handle the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result

# Example usage:
solution = Solution()
print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))  # Output: ["0->2","4->5","7"]
print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # Output: ["0","2->4","6","8->9"]
