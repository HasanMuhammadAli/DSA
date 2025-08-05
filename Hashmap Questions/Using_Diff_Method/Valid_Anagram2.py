'''
Name: Muhammad Ali Mosin Hasan
Date: 4/8/25
Problem: 242: Valid Anagram
'''
'''
Slower way to check if two strings are anagrams by sorting them.
'''

def is_anagram1(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t

# Example usage
s1 = "anagram"  
t1 = "nagaram"
result1 = is_anagram1(s1, t1)
print("Are the strings anagrams?", result1)
# Output: Are the strings anagrams? True