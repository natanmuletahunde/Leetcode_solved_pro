var longestPalindrome = function(s) {
    if (s.length === 0) return "";
    
    let start = 0, end = 0;
    
    // Function to expand around the center and return the length of the palindrome
    const expandAroundCenter = (s, left, right) => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        // return the length of the palindrome
        return right - left - 1;
    };

    for (let i = 0; i < s.length; i++) {
        // Odd length palindromes (center is one character)
        let len1 = expandAroundCenter(s, i, i);
        // Even length palindromes (center is between two characters)
        let len2 = expandAroundCenter(s, i, i + 1);
        let len = Math.max(len1, len2);

        if (len > end - start) {
            // Update the start and end indices of the current longest palindrome
            start = i - Math.floor((len - 1) / 2);
            end = i + Math.floor(len / 2);
        }
    }

    // Return the longest palindrome substring
    return s.substring(start, end + 1);
};

// Example usage:
console.log(longestPalindrome("babad")); // Output: "bab" or "aba"
console.log(longestPalindrome("cbbd"));  // Output: "bb"
