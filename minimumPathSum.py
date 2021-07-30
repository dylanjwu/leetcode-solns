class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def minSum(grid, i, j):
            if i == len(grid) or j == len(grid[0])i-: 
                return grid[i][j]
            if dp[i][j] == -1:
                dp[i][j] =  min(grid[i][j]+minSum(grid, i, j+1), grid[i][j]+minSum(grid, i+1, j))
            return dp[i][j]
        return minSum(grid, 0, 0) 
                                   