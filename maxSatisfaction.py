class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s = sorted(satisfaction, reverse=True)
        # clever greedy solution filched from discussion page
        summ = 0
        total = 0
        for i in range(len(s)):
            if s[i] + summ < 0:
                break     
            summ += s[i]
            total += summ
        return total
