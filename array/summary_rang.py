class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums:
            return ranges
        
        start = nums[0]
        end = nums[0]
        
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                # Append the current range
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                # Reset start and end for the new range
                start = end = num
        
        # Append the final range
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))
        
        return ranges

# Example usage:
sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))  # Output: ["0->2","4->5","7"]
print(sol.summaryRanges([0,2,3,4,6,8,9]))  # Output: ["0","2->4","6","8->9"]
