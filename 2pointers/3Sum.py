def threeSum(nums):
    nums.sort()
    ans = []
    seen = set()
    n = len(nums)
    if n < 3:
        return []
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            if (nums[i] + nums[j] + nums[k]) > 0 :
                k -= 1
                continue
            elif (nums[i] + nums[j] + nums[k]) < 0 :
                j += 1
                continue
            elif (nums[i] + nums[j] + nums[k]) == 0 :
                if tuple([nums[i], nums[j], nums[k]]) not in seen:
                    ans.append([nums[i], nums[j], nums[k]])
                    seen.add(tuple([nums[i], nums[j], nums[k]]))
            j += 1
            k -= 1

    return ans
