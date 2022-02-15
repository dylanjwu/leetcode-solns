class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        money = [0 for _ in nums] 
        money[0], money[1] = nums[0], nums[1]
        
        global_max = max(money[0:2])
        
        for i in range(2, len(nums)):
            for j in range(0, i-1):
                money[i] =  max(money[i], nums[i] + money[j])

            global_max = max(global_max, money[i]) 
            
        return global_max
