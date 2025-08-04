'''
Name: Muhammad Ali Mosin Hasan
Date: 3/8/25
Problem: 217:  Contains Duplicate
'''
from collections import Counter
def containsDuplicate(nums):

    '''
    #using a set to check for duplicates
    h = set()  
    for num in nums:
        if num in h:  
            return True
        else:
            h.add(num)  # Add the number to the set
    return False  # No duplicates found
    '''

    #using Counter from collections to check for duplicates
    counter = Counter(nums)  
    for count in counter.values():
        if count > 1:
            return True  # Found a duplicate
    return False
    

# Example usage
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print("Contains duplicate:", result)  # Output: True
nums = [1, 2, 3, 4]
result = containsDuplicate(nums)
print("Contains duplicate:", result)  # Output: False