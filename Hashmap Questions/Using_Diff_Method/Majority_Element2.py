'''
Name: Muhammad Ali Mosin Hasan
Date: 7/8/25
Problem: 169: Majority Element
'''

#solution 1 using Counter
from collections import defaultdict
def majorityElement(nums):
    '''
    Finds the majority element in the list of numbers using Counter.
    '''
    count = defaultdict(int)
    n = len(nums)

    for num in nums:
        count[num] += 1
        if count[num] > n // 2:
            return num
    return None
# Example usage
nums = [3, 2, 3, 2, 2, 3, 2]
result = majorityElement(nums)
print("Majority Element in Solution: " + str(result))    
