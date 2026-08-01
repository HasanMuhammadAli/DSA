def threeSumClosest(nums, target):
    nums.sort()
    ans = float('inf')
    n = len(nums)

    for i in range(n-2):
        j = i+1
        k = n-1

        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum == target:
                return curr_sum

            if abs(curr_sum - target) < abs(ans - target):
                ans = curr_sum

            if curr_sum > target:
                k -=1 
            elif curr_sum < target:
                j += 1

    return ans

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], target = 1))