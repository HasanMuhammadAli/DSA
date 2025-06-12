'''
Name: Muhammad Ali Mosin Hasan
Date: 12/6/25
Problem: 383: Ransom Note
'''


def canConstruct(ransomNote, magazine):
    '''
    Determines if a ransom note can be constructed from the letters in a magazine.

    Args:
        ransomNote (str): The ransom note to be constructed.
        magazine (str): The magazine containing letters.

    Returns:
        bool: True if the ransom note can be constructed, False otherwise.
    '''
    counter = {}
    # Count occurrences of each letter in the magazine
    for letter in magazine:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    # Check if each letter in the ransom note can be constructed
    for letter in ransomNote:
        if letter not in counter:
            return False
        elif counter[letter] == 1: 
            del counter[letter]
        else:
            counter[letter] -= 1
    return True

# Example usage 
ransomNote = "a"
magazine = "bbaaa"
# Test the function
result = canConstruct(ransomNote, magazine)
print("Can construct ransom note:", result)  # Output: False
ransomNote = "aa"
magazine = "aab"
# Test the function
result = canConstruct(ransomNote, magazine)
print("Can construct ransom note:", result)  # Output: True
ransomNote = "aa"
magazine = "ab"
# Test the function
result = canConstruct(ransomNote, magazine)
print("Can construct ransom note:", result)  # Output: False
