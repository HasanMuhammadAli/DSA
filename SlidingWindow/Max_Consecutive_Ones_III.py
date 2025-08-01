'''
Name: Muhammad Ali Mosin Hasan
Date: 1/8/25
Problem: 1004: Max Consecutive Ones III
'''

def longest_ones(nums, k):
    max_w = 0
    num_zeros = 0
    l = 0
    n = len(nums)

    for r in range(n):
        if nums[r] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1
        
        w = r - l + 1
        max_w = max(max_w, w)

    return max_w

#Example usage:

nums = [1,1,0,0,1,1,1,0,1]
k = 2
print(longest_ones(nums, k))# Output: 7

