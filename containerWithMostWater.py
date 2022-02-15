class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo=0; hi = len(height)-1
        max_volume = 0
        
        while lo < hi:
            volume = (hi-lo)*min(height[lo], height[hi])
            max_volume = max(max_volume, volume)
            if height[lo] < height[hi]:
                lo += 1  
            else:
                hi -= 1
                
        return max_volume
            
