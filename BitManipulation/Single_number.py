'''
Name: Muhammad Ali Mosin Hasan
Date: 29/7/25
Problem: 136: Single Number
'''

def singleNumber(nums):
    """
    Find the single number in an array where every other number appears twice.
    """
    
    a = 0
    for x in nums:
        a ^= x
    
    return a

# Example usage:
nums = [2, 2, 1]
print(singleNumber(nums))  # Output: 1
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4