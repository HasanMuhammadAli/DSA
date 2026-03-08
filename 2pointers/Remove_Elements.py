def removeElement(nums, val):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums= [3,2,2,3]
val = 3
print(removeElement(nums, val))
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))