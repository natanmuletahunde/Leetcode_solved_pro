class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting point has an obstacle, no path is possible
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Initialize the DP array with 0s
        dp = [[0] * n for _ in range(m)]
        
        # The starting position (0,0) has one way to be reached (the robot starts there)
        dp[0][0] = 1
        
        # Initialize the first column (if there's no obstacle)
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Initialize the first row (if there's no obstacle)
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
     
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # No obstacle
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The value at the bottom-right corner is the result
        return dp[m-1][n-1]
