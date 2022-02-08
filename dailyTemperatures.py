class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        result = [0 for _ in temperatures]
        
        
        for i,temp in enumerate(temperatures):
            
            while stack and stack[-1][0] < temp:
                top = stack.pop()
                result[top[1]] = i-top[1]
                    
            stack.append((temp, i))
            
        return result
