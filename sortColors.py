class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return 
        self.easyWay(nums)
        
    def easyWay(self, nums):
        buckets = [0,0,0]
        for num in nums:  
            buckets[num] += 1
        i = 0
        for index,bucket in enumerate(buckets):
            while bucket > 0:
                nums[i] = index
                i += 1
                bucket -= 1
        return nums
      