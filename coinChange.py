class Solution:
    res = []
    def coinChange(self, coins: List[int], amount: int) -> int:
        def cc(coins, i,  k, dp):
            if k == 0:
                return 0

            if k < 0 or i >= len(coins):
                return sys.maxsize

            if dp[i][k] == -1:
                stay = 1 + cc(coins, i, k-coins[i], dp)
                move = cc(coins, i+1, k, dp)
                dp[i][k] = min(stay, move)
            return dp[i][k]
        
        dp = [[-1]*(amount+1) for _ in coins]
        result = cc(coins, 0, amount, dp)
        if result > amount:
            return -1 
        return result
