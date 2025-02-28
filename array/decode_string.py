class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit numbers
            elif char == "[":
                stack.append(current_str)
                stack.append(num)
                current_str = ""  
                num = 0  
            elif char == "]":
                count = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + current_str * count  #
            else:
                current_str += char 

        return current_str
