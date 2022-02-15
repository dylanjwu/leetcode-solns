

"""
IN-PROGRESS; solution not correct
"""

class Solution:
    
    
    def largestRectangleArea(self, heights: List[int]) -> int:
            
        inc_stack = []
        
        max_area = 0
        
        count = 1
        global_count = 1
        min_item = heights[0]
        
        for i,height in enumerate(heights):
            print(inc_stack)
            print(global_count)
            min_item = min(min_item, height)
            if not inc_stack or height >= inc_stack[-1]:
                inc_stack.append(height)
            else:
                area = 0 
                count = 1
                while inc_stack and inc_stack[-1] > height:
                    area = count * inc_stack.pop()
                    max_area = max(area, max_area)
                    count += 1
                global_count += count 
                
        print(inc_stack)         
        min_item = 0
        area = 0 
        res_area = 0
        count = 0
        for i in range(0, len(inc_stack)):
            res_area = inc_stack[i]*(len(inc_stack)-i)
            max_area = max(res_area, max_area, global_count)
            count += 1
            
        global_count += count
            
             
        return max(max_area, global_count*min_item) 
                     
  
