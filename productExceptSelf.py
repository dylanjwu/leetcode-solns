class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        arr = []
        for a in nums:
            arr.append(left_prod)
            left_prod *= a
        
        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] = right_prod * arr[i]
            right_prod *= nums[i]
            
        return arr
        
            
