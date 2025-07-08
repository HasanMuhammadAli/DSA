'''
Name: Muhammad Ali Mosin Hasan
Date: 8/7/25
Problem: 1544: Make The String Great
'''

def isGood(s):
    stk = []
    for c in s:
        if stk and (ord(stk[-1]) - ord(c) == 32 or ord(stk[-1]) - ord(c) == -32):
            stk.pop()
        else:
            stk.append(c)
    return ''.join(stk)

s = "leEeetcode"
print(isGood(s))
s = "abBAcC"
print(isGood(s))
