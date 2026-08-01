def fourSum(nums, target):
    n = len(nums)
    seen = set()
    nums.sort()
    ans = []
    if n < 4:
        return []

    for i in range(n-3):
        for j in range(i+1, n-2):
            k = j+1
            l = n-1
            while k < l:
                curr_sum = nums[i]+nums[j]+nums[k]+nums[l]
                if curr_sum == target:
                    tu = tuple([nums[i], nums[j], nums[k], nums[l]])
                    if tu not in seen:
                        seen.add(tu)
                        ans.append([nums[i], nums[j], nums[k], nums[l]])

                elif curr_sum > target:
                    l -= 1
                    continue

                elif curr_sum < target:
                    k += 1
                    continue

                k += 1
                l -= 1

    return ans

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))
nums = [2,2,2,2,2]
target = 8
print(fourSum(nums, target))