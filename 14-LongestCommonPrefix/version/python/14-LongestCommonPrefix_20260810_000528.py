# Last updated: 8/10/2026, 12:05:28 AM
1class Solution:
2    def longestCommonPrefix(self, strs):
3        prefix = strs[0]
4
5        for s in strs[1:]:
6            while not s.startswith(prefix):
7                prefix = prefix[:-1]
8
9                if prefix == "":
10                    return ""
11
12        return prefix
13        