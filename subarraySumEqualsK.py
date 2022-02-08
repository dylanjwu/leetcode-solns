class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mp = { 0 : 1 } # for the case in which nums[0] = k
        summ = 0
        count = 0
        
        for i in range(len(nums)):
            summ += nums[i] 
            
            if mp.get(summ-k):
                count += mp.get(summ-k)
            
            mp[summ] = mp.get(summ, 0) + 1
            
        return count
                
            
