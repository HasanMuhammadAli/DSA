def reverseString(s):
    n = len(s)
    l, r = 0, n-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l+=1
        r-=1
    print(s)
    
s = ["h","e","l","l","o"]
print(reverseString(s))