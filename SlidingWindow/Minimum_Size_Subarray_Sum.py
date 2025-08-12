'''
Name: Muhammad Ali Mosin Hasan
Date: 12/8/25
Problem: 209: Minimum Size Subarray Sum
'''

def minSubArrayLen(target, nums):
    min_length = float('inf')
    l = 0
    sum = 0

    for r in range(len(nums)):
        sum += nums[r]

        while sum >= target:
            min_length = min(min_length, r - l + 1)

            sum -= nums[l]
            l += 1

    return min_length if min_length != float('inf') else 0

#Example testcase:
print(minSubArrayLen(7, [2,3,1,2,4,3])) #Output: 2
print(minSubArrayLen(4, [1,4,4])) #Output: 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) #Output: 0
