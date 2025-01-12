class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        # Try all possible splits for the first two numbers
        for i in range(1, n // 2 + 1):  # First number's length
            for j in range(i + 1, min(i + (n - i) // 2 + 1, n)):  # Second number's length
                # Extract the first two numbers
                num1 = num[:i]
                num2 = num[i:j]
                
                # If the numbers have leading zeros (except the number "0"), skip this split
                if (num1[0] == '0' and len(num1) > 1) or (num2[0] == '0' and len(num2) > 1):
                    continue
                
                # Now, try to generate the additive sequence
                while j < n:
                    # Calculate the sum of the first two numbers
                    num3 = str(int(num1) + int(num2))
                    
                    # If the sum doesn't match the next part of the string, break
                    if not num.startswith(num3, j):
                        break
                    
                    # Update the sequence for the next iteration
                    num1, num2 = num2, num3
                    j += len(num3)
                    
                    # If we have used all characters and formed a valid sequence, return True
                    if j == n:
                        return True
        
        # If no valid sequence is found, return False
        return False
