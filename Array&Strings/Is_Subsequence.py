'''
Name: Muhammad Ali Mosin Hasan
Date: 12/7/25
Problem: 392: Is Subsequence
'''

def isSubsequence(s, t):
    '''
    Determines if string s is a subsequence of string t.

    A subsequence is a sequence that can be derived from another string by deleting some or no elements, without changing the order of the remaining elements.

    '''
    S = len(s)
    T = len(t)

    if s == '': return True
    if S > T : return False

    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S-1:
                return True
            j += 1
    
    return False

print(isSubsequence("abc", "ahbgdc"))   # Output: True
print(isSubsequence("axc", "ahbgdc"))   # Output: False