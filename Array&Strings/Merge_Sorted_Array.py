'''
Name: Muhammad Ali Mosin Hasan  
Date: 24/7/25  
Problem: 88: Merge Sorted Array
'''

def merge(nums1, m, nums2, n):
    '''
    Merges two sorted arrays nums1 and nums2 into nums1 in-place.
    The first m elements of nums1 are considered, and nums2 has n elements.
    '''
    x, y = m-1, n-1
    for z in range(m+n-1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        if y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y] 
            y -= 1

    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m1 = 3
nums2 = [2, 5, 6]
n1 = 3
result1 = merge(nums1, m1, nums2, n1)
print(result1)  # Output: [1, 2, 2, 3, 5, 6]