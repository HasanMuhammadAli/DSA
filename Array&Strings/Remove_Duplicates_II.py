'''
Name: Muhammad Ali Mosin Hasan  
Date: 23/7/25  
Problem: 80: Remove Duplicates from Sorted Array II
'''

def removeDuplicates(nums):
    '''
    Removes duplicates from a sorted list in-place, allowing at most two occurrences of each element.
    '''
    n = len(nums)
    j = 1
    count = 1
    
    for i in range (1, n):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[j] = nums[i]
            j += 1

    return j

nums1 = [1, 1, 1, 2, 2, 3]
k1 = removeDuplicates(nums1)
print(k1)  # Output: 5, nums1 becomes [1, 1, 2, 2, 3]

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = removeDuplicates(nums2)
print(k2)  # Output: 7, nums2 becomes [0, 0, 1, 1, 2, 3, 3]