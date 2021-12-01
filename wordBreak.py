#this is a 'hard' problem: https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s)+1)]
        
        for i in range(1, len(dp)):
            for j in range(0, i):
                if s[j:i] in wordDict:
                    if j == 0:
                        dp[i].append(s[j:i])
                    elif dp[j] != []:
                        for arr in dp[j]:
                            dp[i].append(arr + " " + s[j:i])
        return dp[-1]
