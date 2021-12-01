class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        totalCost = 0
        
        sameCharsNum = 0
        sameCharsSum = 0
        sameCharsMax = 0
        last = None
        for i in range(0, len(s)):
            if s[i] != last:
                if sameCharsNum > 1:
                    totalCost += sameCharsSum - sameCharsMax
                sameCharsNum = 1
                sameCharsSum = cost[i]
                sameCharsMax = cost[i] 
            else:
                sameCharsNum += 1
                sameCharsSum += cost[i]
                sameCharsMax = max(sameCharsMax, cost[i])
            last = s[i]     
               
        return totalCost + ((sameCharsSum - sameCharsMax) if sameCharsNum > 1 else 0)
                
