class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while True:
            i = (left + right) // 2  # partition nums1
            j = half - i  # partition nums2

            nums1Left = nums1[i - 1] if i > 0 else float('-infinity')
            nums1Right = nums1[i] if i < m else float('infinity')
            nums2Left = nums2[j - 1] if j > 0 else float('-infinity')
            nums2Right = nums2[j] if j < n else float('infinity')

            # Binary search condition
            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total % 2 == 0:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2.0
                else:
                    return min(nums1Right, nums2Right)
            elif nums1Left > nums2Right:
                right = i - 1
            else:
                left = i + 1
