class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        if len(nums) == 1:
            return [copy.copy(nums)]
        
        for i in nums:
            curr_num = nums.pop(0)
            permutations = self.permuteUnique(nums)
            for perm in permutations:
                perm.append(curr_num)
                if perm not in result:
                    result.append(perm) 
            #result.extend(permutations)
            nums.append(curr_num)
            
        return result
            