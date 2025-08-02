'''
Name: Muhammad Ali Mosin Hasan
Date: 2/8/25
Problem: 3: Longest Substring Without Repeating Characters
'''

def lengthOfLongestSubstring(s):
    '''Find the length of the longest substring without repeating characters.'''
    l = 0
    longest = 0
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        
        w = r - l + 1
        longest = max(longest, w)
        sett.add(s[r])

    return longest

# Example usage:
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3

s = "bbbbb"
print(lengthOfLongestSubstring(s))  # Output: 1