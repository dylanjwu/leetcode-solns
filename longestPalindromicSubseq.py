class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def iterate(s):
            #r_s = s[::-1]
            length = len(s)+1
            dp = [[0 for _ in range(length)] for _ in range(length)]
            for i in range(1, length):
                for j in range(length-1, 0, -1):
                    _j = length+2-j
                    if s[i-1] == s[j-1]:
                        dp[i][_j] = 1+dp[i-1][_j-2]
                    else:
                        dp[i][_j] = max(dp[i][_j-1], dp[i-1][_j])
            print(dp)
            return dp[-1][-1]
            
                
            
            
            
        def recurse(s, lo, hi, dp):
            if lo > hi:
                return 0 
            if lo == hi:
                return 1
            
            if dp[lo][hi] != -1:
                return dp[lo][hi]
            
            if s[lo] == s[hi]:
                dp[lo][hi] = 2+recurse(s, lo+1, hi-1, dp)
                
            else:
                left = recurse(s, lo+1, hi, dp)
                right = recurse(s, lo, hi-1, dp)
                dp[lo][hi] = max(left, right)
                
            return dp[lo][hi]
        
        dp = [[-1 for _ in s] for _ in s]
        return iterate(s)
        #return recurse(s, 0, len(s)-1, dp)
            
