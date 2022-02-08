class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        running_sum = 0
        mp = {}
        result = []
        for i, num in enumerate(nums):
            running_sum += num 
            print(running_sum, (running_sum-k) % k)
            if (running_sum-k) % k in mp:
                if i-mp[(running_sum-k) % k]+1 >= 2:
                    return True
            else: 
                mp[running_sum % k] = i
            
        return False
                
