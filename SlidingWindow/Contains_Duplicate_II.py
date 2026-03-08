def containsNearbyDuplicate(nums, k):
    # l = 0
    # n = len(nums)
    # sett = set()
    # for r in range(n):
    #     if nums[r] not in sett:
    #         sett.add(nums[r])
    #     elif nums[r] in sett:
    #         while r > l:
    #             if nums[l] == nums[r]:
    #                 return l, r
    #             else:
    #                 l+=1

    l = 0
    n = len(nums)
    sett = set()
    for r in range(n):
        if nums[r] in sett:
            ans = abs(r-l)
            if ans > k:
                sett.remove(nums[l])
                l+=1
            elif ans <= k:
                return True
        sett.add(nums[r])
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))
nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))
# nums = [1,2,3,1,2,3]
# k = 2
# print(containsNearbyDuplicate(nums, k))
# nums = [1,4,2,3,1,2]
# k = 3
# print(containsNearbyDuplicate(nums, k))
