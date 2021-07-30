class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(i, n, k):
            result = []
        
            if k <= 0:
                return [copy.copy(result)]
        
            for j in range(i, n+1):
                combs = helper(j+1, n, k-1)
                for comb in combs:
                    comb.append(j)
                result.extend(combs)
                
            return result
        
        return helper(1, n, k) 
        