class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # Step 1: Mark next states with intermediate values
        for i in range(m):
            for j in range(n):
                # Count live neighbors (cells with 1 or 2)
                live_neighbors = 0
                for di, dj in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in [1, 2]:
                        live_neighbors += 1
                
                # Apply rules
                if board[i][j] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Live -> Dead
                else:  # Dead cell
                    if live_neighbors == 3:
                        board[i][j] = 3  # Dead -> Live
        
        # Step 2: Convert intermediate states to final states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0  # Was live, now dead
                elif board[i][j] == 3:
                    board[i][j] = 1  # Was dead, now live