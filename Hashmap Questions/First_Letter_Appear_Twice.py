'''
Name: Muhammad Ali Mosin Hasan
Date: 27/6/25
Problem: 2351: First Letter to Appear Twice
'''

from collections import defaultdict

def firstLetterAppearTwice(s):
    """
    Find the first character that appears twice in a string.
    
    Given a string s consisting of lowercase English letters, return the first letter 
    to appear twice.
    
    Note: A letter 'a' appears twice before another letter 'b' if the second occurrence 
    of 'a' is before the second occurrence of 'b'. s will contain at least one letter 
    that appears twice.
    
    Args:
        s (str): A string consisting of lowercase English letters
        
    Returns:
        str: The first character that appears twice
        
    """
    counter = defaultdict(int)
    for ch in s:
        counter[ch] += 1
        if counter[ch] == 2:
            return ch
    

s = "abccbaacz"
print(firstLetterAppearTwice(s))    
s = "abcdd"
print(firstLetterAppearTwice(s)) 
