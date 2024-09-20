/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // Ensure nums1 is the smaller array to reduce the binary search space
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    let m = nums1.length;
    let n = nums2.length;
    
    let low = 0, high = m;
    
    while (low <= high) {
        // Partition nums1 and nums2
        let partition1 = Math.floor((low + high) / 2);
        let partition2 = Math.floor((m + n + 1) / 2) - partition1;
        
        // Get the values on the left and right side of the partitions
        let maxLeft1 = (partition1 === 0) ? -Infinity : nums1[partition1 - 1];
        let minRight1 = (partition1 === m) ? Infinity : nums1[partition1];
        
        let maxLeft2 = (partition2 === 0) ? -Infinity : nums2[partition2 - 1];
        let minRight2 = (partition2 === n) ? Infinity : nums2[partition2];
        
        // Check if we have found the correct partition
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            // If the combined length of both arrays is odd
            if ((m + n) % 2 === 1) {
                return Math.max(maxLeft1, maxLeft2);
            } else {
                // If the combined length is even, the median is the average of the two middle values
                return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
            }
        } else if (maxLeft1 > minRight2) {
            // Move left in nums1
            high = partition1 - 1;
        } else {
            // Move right in nums1
            low = partition1 + 1;
        }
    }
    
    throw new Error("Input arrays are not sorted.");
};
