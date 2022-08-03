# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest = 1
        res = s[0]
        for i, c in enumerate(s):
            # even
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > longest:
                    longest = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
            # odd
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r -l + 1 > longest:
                    longest = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
                
        return res