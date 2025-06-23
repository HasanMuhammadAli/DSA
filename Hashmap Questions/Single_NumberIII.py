'''
Name: Muhammad Ali Mosin Hasan
Date: 23/6/25
Problem: 260: Single Number III
'''
from collections import Counter
def single_numberIII(nums):
    '''
    Finds the two numbers that appear only once in the list, while all other numbers appear twice.       
    '''
    ans = []
    count = Counter(nums)
    for key, freq in count.items():
        if freq == 1:
            ans.append(key)
    return ans

# Example usage
nums = [1, 2, 1, 3, 2, 5]
result = single_numberIII(nums)
print("The two numbers that appear only once are:", result)

nums = [-1, 0]
result = single_numberIII(nums)
print("The two numbers that appear only once are:", result)