class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binary_search(nums, lo, hi):
            if lo <= hi:
                mid = (lo+hi)//2
                if lo==hi:
                    return lo
                if nums[mid] < nums[mid+1]:
                    return binary_search(nums, mid+1, hi)
                elif nums[mid] < nums[mid-1]:
                    return binary_search(nums, lo, mid-1)
                else:
                    return mid
        return binary_search(nums, 0, len(nums)-1) 