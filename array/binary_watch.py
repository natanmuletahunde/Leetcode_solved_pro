class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        if turnedOn > 8:  # More LEDs than possible
            return []
        
        result = []
        for hour in range(12):  # Hours range from 0 to 11
            for minute in range(60):  # Minutes range from 0 to 59
                # Count the number of LEDs turned on
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    # Format the time
                    result.append(f"{hour}:{minute:02d}")
        
        return result
