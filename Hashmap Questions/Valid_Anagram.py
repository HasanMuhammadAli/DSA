'''
Name: Muhammad Ali Mosin Hasan
Date: 17/6/25
Problem: 242: Valid Anagram
'''
from collections import Counter


def is_anagram(s, t):
    '''
    Checks if two strings are anagrams of each other using a hashmap.
    '''
    if len(s) != len(t):
        return False
    
    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict
# Example usage
s2 = "rat"
t2 = "car"
result2 = is_anagram(s2, t2)
print("Are the strings anagrams?", result2)
# Output: Are the strings anagrams? False