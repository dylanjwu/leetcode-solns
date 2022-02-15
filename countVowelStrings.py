class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bottomUp(n)
       
        
    def bottomUp(self, n):
        dp = [[0 for _ in range(6)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, 6):
                dp[i][j] += int(i == 1) + dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]
                
    def memoized(self, n):
        dp = [[-1 for _ in range(5)] for _ in range(n)]
        def helper(n, i):
            if n == 0:
                return 1
            if i == 0:
                return 0
            if dp[n-1][i-1] == -1:
                dp[n-1][i-1] = helper(n, i-1)+helper(n-1, i)
            return dp[n-1][i-1]
        return helper(n, 5) 
