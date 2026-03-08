def sortedSquares(nums):
    n = len(nums)
    l = 0
    r = n - 1
    ans = [0]*n
    pos = n-1

    while l <= r:
        if abs(nums[l]) < abs(nums[r]):
            ans[pos] = nums[r] ** 2
            pos -= 1
            r -= 1
        else:
            ans[pos] = nums[l] ** 2
            pos -= 1
            l += 1
    
    return ans
    

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))