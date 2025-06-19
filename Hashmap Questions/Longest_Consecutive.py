'''
Name: Muhammad Ali Mosin Hasan
Date: 19/6/25
Problem: 128: Longest Consecutive Sequence
'''


'''
Finds the length of the longest sequence of consecutive integers in an unsorted list.

Args:
    nums (list): List of integers.

Returns:
    int: Length of the longest consecutive elements sequence.
'''

def longest_consecutive(nums):
    s = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) not in s:
            length = 1
            next_num = num + 1
            while next_num in s:
                length += 1
                next_num += 1
            longest = max(longest, length)
    return longest

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4
nums = [0, 3, 7, 2, 5, 8, -1, 4, 6]
print(longest_consecutive(nums))  # Output: 7
nums = []
print(longest_consecutive(nums))  # Output: 0