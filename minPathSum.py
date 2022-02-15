class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def minSum(grid, i, j):
            if i == 0: 
                row_sum = sum(grid[i][:j+1])
                return row_sum
            if j == 0:
                col_sum = sum([grid[k][j] for k in range(i+1)])
                return col_sum
            if dp[i][j] == -1:
                dp[i][j] =  min(grid[i][j]+minSum(grid, i, j-1), grid[i][j]+minSum(grid, i-1, j))
            return dp[i][j]
        return minSum(grid, len(grid)-1, len(grid[0])-1) 
                                   
