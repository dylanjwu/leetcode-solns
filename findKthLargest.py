class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.kthLargest(nums, k, 0, len(nums)-1) 
    
    def partition(self, nums, lo, hi):
        pivot = nums[hi]
        pp_index = lo
        for i in range(lo, hi):
            if nums[i] > pivot:
                nums[pp_index], nums[i] = nums[i], nums[pp_index]
                pp_index += 1

        nums[pp_index], nums[hi] = nums[hi], nums[pp_index]
        
        return pp_index 
    
    def kthLargest(self, nums, k, lo, hi):
        
        if lo == hi:
            return nums[hi]
        
        pivot_index = self.partition(nums, lo, hi)
        
        if pivot_index == k-1:
            return nums[pivot_index]
        
        if pivot_index < k-1:
            return self.kthLargest(nums, k, pivot_index+1, hi)
        else:
            return self.kthLargest(nums, k, lo, pivot_index-1)
