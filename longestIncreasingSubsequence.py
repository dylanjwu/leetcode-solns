class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        
        globalLIS = 1
        for i in range(1, len(nums)):
            curr = nums[i]
            localLIS = 0
            for j in range(0, i):
                if curr > nums[j]:
                    localLIS = max(localLIS, dp[j])
            dp[i] = 1 + localLIS
            globalLIS = max(dp[i], globalLIS)
        print(dp)   
        return globalLIS
        
        
"""
Attempting to optimize to O(nlogn)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_seen = [nums[0]]
        
        globalLIS = 1
        for i in range(1, len(nums)):
            print(sorted_seen)
            numGreaterThan = self.indexOf(sorted_seen, nums[i])
            
            print(numGreaterThan)
            if numGreaterThan == len(sorted_seen):
                sorted_seen.append(nums[i])
            elif nums[i] != sorted_seen[numGreaterThan-1]:
                print("try to insert")
                sorted_seen.insert(numGreaterThan, nums[i])
            globalLIS = max(numGreaterThan, globalLIS)
        return globalLIS
    
    def indexOf(self, nums, val):
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == val:
                return mid
            elif nums[mid] < val:
                lo = mid+1
            else:
                hi = mid-1
        return lo 
"""
