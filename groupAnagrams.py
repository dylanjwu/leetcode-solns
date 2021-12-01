class Solution:
    
    def radixSort(self,s):
        alpha = [0 for _ in range(26)]
        for ch in s:
            alpha[ord(ch)-97] += 1
        
        res = ""
        for i,count in enumerate(alpha):
            for _ in range(count):
                res += chr(i + 97)
        return res 
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            ssorted = self.radixSort(s)
            if mp.get(ssorted):
                mp[ssorted].append(s)
            else:
                mp[ssorted] = [s]
            
        return list(mp.values())
