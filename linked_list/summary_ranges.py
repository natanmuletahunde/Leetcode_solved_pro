class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:  # Handle the case where nums is empty
            return []

        result = []
        start = nums[0]  # Start of the current range

        for i in range(1, len(nums)):
            # If the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # Add the range to the result
                if start == nums[i - 1]:  # Single number
                    result.append(str(start))
                else:  # Range
                    result.append(f"{start}->{nums[i - 1]}")
                # Update the start for the next range
                start = nums[i]

        # Handle the last range
        if start == nums[-1]:  # Single number
            result.append(str(start))
        else:  # Range
            result.append(f"{start}->{nums[-1]}")

        return result
