# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        i = 0
        ls = ['']*numRows
        sign = 1
        
        for ch in s:
            ls[i]+= ch
            i+=1*sign
            
            if i == numRows:
                i-=2
                sign=-1
            
            if i == -1:
                i+=2
                sign = 1
            
        return ''.join(ls)