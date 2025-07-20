'''
Name: Muhammad Ali Mosin Hasan
Date: 20/7/25
Problem: 75: Sort Colors
'''
def sortColors(nums):
    """
    Sorts the input list nums containing only 0s, 1s, and 2s in-place
    so that all 0s come first, then all 1s, then all 2s.

    
    """
    counts = [0, 0, 0]
    for color in nums:
        counts[color] += 1
    
    R, W, B = counts
    nums[:R] = [0] * R
    nums[R:R+W] = [1] * W
    nums[R+W:] = [2] * B

nums1 = [2, 0, 2, 1, 1, 0]
sortColors(nums1)
print(nums1)  # Output should be: [0, 0, 1, 1, 2, 2]

nums2 = [1, 0, 1, 2, 0, 2]
sortColors(nums2)
print(nums2)  # Output should be: [0, 0, 1, 1, 2, 2]