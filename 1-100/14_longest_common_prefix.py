# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # find the shortest string in the list
        short_str = min(strs, key = len)
        # get the length of shortest string
        short_len = len(short_str)
        
        i = 0
        result = ""
        while i < short_len and all(val == strs[0][i] for val in [x[i] for x in strs]):
            result += strs[0][i]
            i += 1
            
        return result