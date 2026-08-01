def searchInsert(nums, target):
    n = len(nums)
    left = 0
    right = n-1

    while left <= right:
       
        mid = (left + ((right-left)//2))
        #print(M)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
        

    if nums[mid] < target:
        return mid+1
    else:
        if mid == 0:
            return mid

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))
nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))
nums=[1,3,5,6]
target = 0
print(searchInsert(nums, target))
nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))
