def findMaxConsecutiveOnes (nums):
    '''
    Correct but not sliding window (tried to but couldn't make it😭)
    l = 0
    r = 0
    max_ones = 0
    counter = 0
    n = len(nums)

    for r in range(n):
        if nums[r] == 1:
            r += 1
            counter += 1
            max_ones = max(max_ones, counter)

        elif nums[r] == 0:
            l = r
            max_ones = max(max_ones, counter)
            counter = 0

    return max_ones
'''

    l = 0
    max_len = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            l = r+1
        max_len = max(max_len, r-l+1)

    return max_len

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))
nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))
nums = [0,1]
print(findMaxConsecutiveOnes(nums))