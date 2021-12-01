from heapq import heappop, heappush, heapify
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = "" 
        heap = []
        heapify(heap)
        freqs = {}
        
        for ch in s: 
            freqs[ch] = freqs.get(ch, 0) + 1
                
        for key in freqs.keys():
            heappush(heap, (-1 * freqs[key], key))
            
        while heap:
            entry = heappop(heap)
            res += (-1*entry[0]*entry[1])
            
        return res
