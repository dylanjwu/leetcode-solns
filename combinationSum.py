class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        def helper(i, curr):
            if sum(curr) == target:
                results.append(curr)
                return
            if sum(curr) > target:
                return
            
            for j in range(i, len(candidates)):
                helper(j, [candidates[j]] + curr.copy())
                
        helper(0, [])
        return results
            
             
            
