'''
Name: Muhammad Ali Mosin Hasan  
Date: 22/7/25  
Problem: 26: Remove Duplicates from Sorted Array  
'''

def removeDuplicates(nums):
    '''
    Removes duplicates from a sorted list in-place.
    '''
    n = len(nums)
    j = 1  

    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    
    return j


nums1 = [1, 1, 2, 2, 3]
k1 = removeDuplicates(nums1)
print(k1) 

nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums1)
print(k2) 