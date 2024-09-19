/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // Step 1: Handle negative numbers and numbers ending with 0 (except 0 itself)
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }

    // Step 2: Reverse the second half of the number
    let reversedHalf = 0;
    while (x > reversedHalf) {
        reversedHalf = reversedHalf * 10 + x % 10;  // Add the last digit of x to reversedHalf
        x = Math.floor(x / 10);  // Remove the last digit from x
    }

    // Step 3: Check if the first half is equal to the reversed second half
    return x === reversedHalf || x === Math.floor(reversedHalf / 10);
};
