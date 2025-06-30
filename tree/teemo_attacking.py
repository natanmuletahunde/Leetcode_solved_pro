class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or duration == 0:
            return 0
        
        total_time = 0
        
        for i in range(len(timeSeries) - 1):
            # Calculate the time between this attack and the next one
            time_diff = timeSeries[i + 1] - timeSeries[i]
            # Add the minimum between duration and the time_diff
            total_time += min(duration, time_diff)
        
        # Add duration for the last attack
        total_time += duration
        
        return total_time
