'''
Name: Muhammad Ali Mosin Hasan
Date: 16/6/25
Problem: 1:Two Sum
'''

def two_sum(nums, target):
    '''
    Finds indices of two numbers in nums that add up to target.

    Args:
        nums (list): List of integers.
        target (int): Target sum.

    Returns:
        list: Indices of the two numbers that add up to target.
    '''
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    
    for i in range(len(nums)):
        y = target - nums[i]
        if y in h and h[y] != i:
            return [i, h[y]]
    return None
   
# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of numbers that add up to target:", result)
# Output: Indices of numbers that add up to target: [0, 1]

# Example usage with no solution
nums_no_solution = [1, 2, 3]
target_no_solution = 6
result_no_solution = two_sum(nums_no_solution, target_no_solution)
print("Indices of numbers that add up to target (no solution):", result_no_solution)
# Output: Indices of numbers that add up to target (no solution): None