
def firstPalindrome(words):
    for s in words:
        n = len(s)
        if n == 1:
            return "".join(s)
        l = 0
        r = n -1
        flag = 0
        while l < r:
            if s[l] != s[r]:
                flag = 0
                break
            elif s[l] == s[r]:
                l += 1
                r -= 1
                flag = 1
        
        if flag == 1:
            return "".join(s) 
        
    return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))
words = ["notapalindrome","racecar"]
print(firstPalindrome(words))


'''
More optimized version.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            else:
                return s   # loop finished without break → palindrome
        return ""

'''

'''
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if s == s[::-1]:
                return s
        return ""
'''