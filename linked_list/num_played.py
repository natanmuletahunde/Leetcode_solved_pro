class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        def timeToMinutes(t):
            h, m = map(int, t.split(':'))
            return h * 60 + m

        start = timeToMinutes(loginTime)
        end = timeToMinutes(logoutTime)

        # If logoutTime is less than loginTime, it means it goes past midnight
        if end < start:
            end += 24 * 60  # add 1440 minutes

        # Round login up to the next 15-minute mark
        roundedStart = ((start + 14) // 15) * 15
        # Round logout down to the previous 15-minute mark
        roundedEnd = (end // 15) * 15

        # Count full rounds
        return max(0, (roundedEnd - roundedStart) // 15)
