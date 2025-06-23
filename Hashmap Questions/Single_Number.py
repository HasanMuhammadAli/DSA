'''
Name: Muhammad Ali Mosin Hasan
Date: 21/6/25
Problem: 136: Single Number I
'''
from collections import Counter
def single_number(nums):
    count = Counter(nums)
    for key, freq in count.items():
        if freq == 1:
            return key
            #ans.append(key)  if there will be multiple elements that appears once
    #return ans      return that ans list    
nums = [2, 2, 1]
result = single_number(nums)
print("The element which appeared once: ", result)

nums = [4, 1, 2, 1, 2]
result = single_number(nums)
print("The element which appeared once: ", result)
