'''
Name: Muhammad Ali Mosin Hasan
Date: 13/7/25
Problem: 14:  Longest Common Prefix
'''

def longestPrefix(strs):

    min_length = float('inf')
    for str in strs:
        if len(str) < min_length:
            min_length = len(str)
    
    i = 0
    while i < min_length:
        for s in strs:
            if strs[0][i] != s[i]:
                return s[:i] 
        i += 1
    
    return s[:i]

strs = ["flower", "flow", "fl"]
print(longestPrefix(strs))#fl
strs = ["abc", "xyz"]
print(longestPrefix(strs))#empty
strs = ["a"]
print(longestPrefix(strs))#a