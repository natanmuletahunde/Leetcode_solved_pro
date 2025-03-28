class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize with a large value

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is exactly the target, return it
                if current_sum == target:
                    return current_sum

                # Update the closest sum if the current sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                # Move pointers based on the sum
                if current_sum < target:
                    left += 1  # Increase the sum by moving the left pointer
                else:
                    right -= 1  # Decrease the sum by moving the right pointer

        return closest_sum
