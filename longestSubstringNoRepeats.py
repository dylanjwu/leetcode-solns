class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        maximum = 0
        curr = ""
        seen = {}
        for i in range(len(s)):
            
            if s[i]: 
                curr += ch
                seen[ch] = 1
                maximum = max(maximum, len(curr))
            else:
                curr += s[i]
                seen[s[i]] = i+1
                curr = curr[i+1:]
                
        return max(maximum, len(curr))
        