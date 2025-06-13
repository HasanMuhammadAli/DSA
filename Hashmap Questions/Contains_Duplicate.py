'''
Name: Muhammad Ali Mosin Hasan
Date: 13/6/25
Problem: 217:  Contains Duplicate
'''

def containsDuplicate(nums):
    '''
    Checks if there are any duplicates in the list of numbers.

    Args:
        nums (List[int]): List of integers to check for duplicates.

    Returns:
        bool: True if there are duplicates, False otherwise.
    '''
    h = set()  # Create a set to store numbers
    for num in nums:
        if num in h:  # If the number is already in the set, it's a duplicate
            return True
        else:
            h.add(num)  # Add the number to the set
    return False  # No duplicates found

# Example usage
nums = [1, 2, 3, 1]
# Test the function
result = containsDuplicate(nums)
print("Contains duplicate:", result)  # Output: True
nums = [1, 2, 3, 4]
# Test the function
result = containsDuplicate(nums)
print("Contains duplicate:", result)  # Output: False