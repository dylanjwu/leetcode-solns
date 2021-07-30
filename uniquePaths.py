class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #bottom-up 
        return self.bottom_up(m, n)
        
        #memoized 
        #dp = [[-1 for _ in range(n)] for _ in range(m)]
        #return self.memoized(m-1, n-1, dp)
        
    def memoized(self, m, n, dp):
        if m == 0 or n == 0:
            return 1
        if dp[m][n] == -1:
            dp[m][n] = self.memoized(m, n-1, dp) + self.memoized(m-1, n, dp)
        return dp[m][n]
    
    def bottom_up(self, m, n):
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        print(matrix)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix[i][j]=1
                else:
                    matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
        return matrix[-1][-1]