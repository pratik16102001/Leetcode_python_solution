# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

import re
class Solution(object):
    def isMatch(self, s, p):
        m = re.search(p,s)
        return False if m is None else len(m.group()) == len(s)