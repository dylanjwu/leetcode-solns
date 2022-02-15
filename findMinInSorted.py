class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0; hi = len(nums)-1
        
        while lo <= hi:
            mid=lo+(hi-lo)//2
            if nums[mid] < nums[hi]:
                hi = mid#this, not mid-1, b/c we need to include the element nums[mid] for contention as min
            else:
                lo = mid+1
        return nums[mid]
