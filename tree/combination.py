class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, curr_comb, results):
            # Base case: if current combination has k numbers, add to results
            if len(curr_comb) == k:
                results.append(curr_comb[:])
                return
            
            # Try each number from 'start' to n
            for i in range(start, n + 1):
                # Add current number to combination
                curr_comb.append(i)
                # Recurse with next number (i+1) to avoid duplicates
                backtrack(i + 1, curr_comb, results)
                # Backtrack: remove the number to try next option
                curr_comb.pop()
        
        results = []
        backtrack(1, [], results)
        return results