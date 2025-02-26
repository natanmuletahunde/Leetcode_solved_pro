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
                current_str = ""  # Reset for the new substring
                num = 0  # Reset number
            elif char == "]":
                count = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + current_str * count  # Decode substring
            else:
                current_str += char  # Append letters

        return current_str
