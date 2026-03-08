def validPalindrome(s):
    n = len(s)
    l = 0
    r = n - 1
    flag = 0
'''
1 thing missing what if we have to remove s[l] to get palindrome string
    while l < r and n > 0:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] != s[r] and flag == 0:
            r -= 1
            flag = 1
        elif s[l] != s[r] and flag == 1:
            return False
    return True
'''

def validPalindrome(s):
    
    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    l = 0
    r = len(s) - 1
    
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            # Try skipping either left OR right
            return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
    
    return True

s = "aba"
print(validPalindrome(s))
s = "abca"
print(validPalindrome(s))
s = "abc"
print(validPalindrome(s))
        
