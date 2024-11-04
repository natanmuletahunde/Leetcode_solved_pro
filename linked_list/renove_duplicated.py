class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check if the list is empty
        if not nums:
            return 
        
        # Initialize the pointer for the unique elements
        k = 1  # Start from the second element
        
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Update the next position for unique element
                k += 1  # Move the unique pointer
        
        return k  # Return the number of unique elements

# Example usage:
solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)

print(k)  # Output: 5
print(nums[:k])  # Output: [0, 1, 2, 3, 4]
