class Solution(object):
    def subsets(self, nums):
        return self.iterative(nums)

    def recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = []
        
        if len(nums) == 0:
            return [[]]
            
        for i, num in enumerate(nums):
            subsets = self.recursive(nums[i+1:]) 
            for s in subsets:
                s.append(num)
            powerset.extend(subsets)
        powerset.append([])    
        
        return powerset
    
    def iterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = []
        stack = [[i] for i in range(len(nums))]
        
        while stack:
            curr = stack.pop()
            powerset.append([nums[c] for c in curr])      
            for i in range(curr[-1]+1, len(nums)):
                stack.append(curr+[i])
                
        powerset.append([])
        return powerset
                
            