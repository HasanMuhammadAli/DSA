def sortArrayByParity(nums):
    n = len(nums)
    l, r = 0, n-1
    while l < r and n > 0:
        if nums[l] % 2 == 0:
            l += 1
        elif nums[l] % 2 != 0 and nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        else:
            l += 1
            r -= 1
    return nums

nums =[1,3]
print(sortArrayByParity(nums))
nums = [3,1,2,4]
print(sortArrayByParity(nums))
nums = [0]
print(sortArrayByParity(nums))