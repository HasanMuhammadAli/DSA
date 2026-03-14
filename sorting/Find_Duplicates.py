## O(nlogn)
# def findDuplicates(nums):
#     nums.sort()
#     i = 0
#     n = len(nums)
#     while i < n- 2:
#         if nums[i] == nums[i+1]:
#             nums.append(nums[i])
#             i += 1
#         i += 1
    
#     return nums[n:]


##O(n)
def findDuplicates(nums):
    result = []
    for x in nums:
        idx = abs(x) - 1
        # If the value at that index is negative, we've seen this number before
        if nums[idx] < 0:
            result.append(abs(x))
        else:
            # Mark it as seen by making it negative
            nums[idx] *= -1
            
    return result

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
nums = [1,1,2]
print(findDuplicates(nums))
nums = [1]
print(findDuplicates(nums))