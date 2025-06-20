'''
Name: Muhammad Ali Mosin Hasan
Date: 20/6/25
Problem: 169: Majority Element
'''

#solution 1 using Counter
from collections import Counter
def majorityElement1(nums):
    '''
    Finds the majority element in the list of numbers using Counter.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: The majority element.
    '''
    count = Counter(nums)
    n = len(nums)

    for key, freq in count.items():
        if freq > n//2:
            return key
    return None

# Example usage
nums = [3, 2, 3]
result = majorityElement1(nums)
print("Majority Element using Counter: " + str(result)) 

#solution 2 
def majorityElement2(nums):
    '''
    Finds the majority element in the list of numbers 
    '''
    ans = -1
    count = 0 

    for num in nums:
        if count == 0:
            ans = num
        if ans == num:
            count += 1
        else:
            count -= 1
    return ans

# Example usage
nums = [3, 2, 3, 2, 2, 3, 2]
result = majorityElement2(nums)
print("Majority Element in Solution2: " + str(result))    
