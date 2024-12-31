class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []  # Handle the case where nums is empty

        result = []
        start = nums[0]  # Start of the current range

        for i in range(1, len(nums)):
            # Check if the current number is not contiguous
            if nums[i] != nums[i - 1] + 1:
                # Add the range to the result
                if start == nums[i - 1]:
                    result.append(str(start))  # Single number range
                else:
                    result.append(f"{start}->{nums[i - 1]}")  # Multi-number range
                # Update the start of the next range
                start = nums[i]

        # Add the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result
