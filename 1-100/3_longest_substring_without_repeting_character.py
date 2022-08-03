# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        subc = 0
        d = {}
        for i, c in enumerate(s):
            subc+=1 
            if d.get(c)!=None:
                if subc > i -d[c]:
                    subc = i - d[c]
            if count < subc:
                count = subc
            d[c] = i
            
        return count