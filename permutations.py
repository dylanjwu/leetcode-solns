class Solution(object):

    perms = []
    def permute_ver3(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        s = [[num] for num in nums] 
        result = []
        
        while s:
            curr = s.pop()
            for node in nums:
                if node not in curr:
                    newList = curr + [node]
                    if len(newList) == len(nums):
                        result.append(newList)
                    else:
                        s.append(newList)
                    
                        
        return result

    def permute_ver2(self, nums: List[int]) -> List[List[int]]:
        def recurse(curr):
            if len(nums) == 0:
                perms.append(curr)
                return
            for num in nums:
                a = nums.pop(0)
                recurse([a]+curr.copy()) 
                nums.append(a)
        recurse([])
        return perms


    def permute_ver1(self, nums: List[int]) -> List[List[int]]:
        result = [] # the list of lists (permutations) to return

        # base case
        if len(nums) == 1:
            return [nums.copy()] # copy here is crucial. Why?
        
        for num in nums: 
            n = nums.pop(0) # remove current number from the nums list
            perms = self.permute(nums) # get the permutation of nums w/o n
            for perm in perms: # add n to end of each permutation (save some time relative to adding it to the front)
                perm.append(n)
            result.extend(perms) # add permutations of n to the result
                                 # this is only added when all permutations for n have been added
            nums.append(n) # add n back to nums so that it can be used for other permutations of different n's.

        return result #this only runs when all permutations have been added