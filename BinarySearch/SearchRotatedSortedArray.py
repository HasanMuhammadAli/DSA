def search(nums, target):
    #Binary Search Algo
    def biSearch(left, right):
        while left <= right:
            mid = left +((right-left)//2)
            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                right = mid-1

            else:
                left = mid+1

        return -1
    
    n = len(nums)
    left = 0
    right = n-1

    #Finding pivot
    while left < right:
        mid = left +((right-left)//2)
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid

    pivot = left

    #Finding target index
    if pivot == 0:
        return biSearch(0, n-1)

    if target >= nums[0] and target <= nums[pivot-1]:
        return biSearch(0, pivot-1)

    else:
        return biSearch(pivot, n-1)



nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))

nums = [1]
target = 0
print(search(nums, target))
