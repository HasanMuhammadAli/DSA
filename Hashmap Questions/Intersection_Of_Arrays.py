'''
Name: Muhammad Ali Mosin Hasan
Date: 20/6/25
Problem: 349: Intersection of Two Arrays
'''

#solution 1 using set
def intersection1(nums1, nums2):
    '''
    Finds the intersection of two arrays using set.
    '''
    s1 = set(nums1)
    s2 = set(nums2)
    result = []
    for num in s1:  
        if num in s2:
            result.append(num)
    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection1(nums1, nums2)
print(f"nums1: {nums1}")
print(f"nums2: {nums2}")
print(f"Intersection: {result}")
print(f"Expected: [2]")
print()

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersection1(nums1, nums2)
print(f"nums1: {nums1}")
print(f"nums2: {nums2}")
print(f"Intersection: {result}")
print(f"Expected: [4, 9] (order may vary)")
print()