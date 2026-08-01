def isPalindrome(s):
    n = len(s)
    l = 0
    r = n-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "race a car"
print(isPalindrome(s))