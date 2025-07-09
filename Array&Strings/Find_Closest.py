'''
Name: Muhammad Ali Mosin Hasan
Date: 9/7/25
Problem: 2239: Find Closest Number to Zero
'''

def findClosestNumber(nums):
    '''
    Returns the number in the list 'nums' that is closest to zero.
    If two numbers are equally close to zero, the function returns the positive one.
    The function first finds the number with the smallest absolute value,
    and if that number is negative and its positive counterpart exists in the list, it returns the positive counterpart instead.
    '''
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
    
    if closest < 0 and abs(closest) in nums: 
        return abs(closest)
    else:
        return closest

nums = [-2, 3]
print(findClosestNumber(nums))