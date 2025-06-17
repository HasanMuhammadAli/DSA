'''
Name: Muhammad Ali Mosin Hasan
Date: 17/6/25
Problem: 242: Valid Anagram
'''
from collections import Counter
#way1
def is_anagram1(s, t):
    '''
    Checks if two strings are anagrams of each other.

    Args:
        s (str): First string.
        t (str): Second string.

    Returns:
        bool: True if s and t are anagrams, False otherwise.
    '''
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t
# Example usage
s1 = "anagram"  
t1 = "nagaram"
result1 = is_anagram1(s1, t1)
print("Are the strings anagrams (way1)?", result1)
# Output: Are the strings anagrams (way1)? True

#way2
def is_anagram2(s, t):
    '''
    Checks if two strings are anagrams of each other using a hashmap.

    Args:
        s (str): First string.
        t (str): Second string.

    Returns:
        bool: True if s and t are anagrams, False otherwise.
    '''
    if len(s) != len(t):
        return False
    
    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict
# Example usage
s2 = "rat"
t2 = "car"
result2 = is_anagram2(s2, t2)
print("Are the strings anagrams (way2)?", result2)
# Output: Are the strings anagrams (way2)? False