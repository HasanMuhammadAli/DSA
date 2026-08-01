
# def combinationSum2(candidates, target):
#     n = len(candidates)
#     candidates = sorted(candidates)
#     curr_sum = 0
#     res, sol = [], []
#     sett = set()
#     def backtrack(i, curr_sum):
#         if curr_sum == target:
#             tu = tuple(sol[:])
#             if tu not in sett:
#                 res.append(sol[:])
#                 sett.add(tu)

        
#         if curr_sum > target:
#             return
        
#         if i == n:
#             return
        
#         #Don't Choose
#         backtrack(i+1, curr_sum)

#         #Choose
#         sol.append(candidates[i])
#         backtrack(i+1, curr_sum + candidates[i])
#         sol.pop()
    
#     backtrack(0, 0)
#     return res


# print(combinationSum2([2,5,2,1,2], 5))


# def combinationSum3(k, n):
#     res, sol = [], []
#     seen = set()
#     def backtrack(i, curr_sum):
#         if curr_sum == n and len(sol) == k:
#             #if sorted(sol[:]) not in seen:
#             res.append(sol[:])
#                 #seen.add(sorted(sol[:]))
#             return

#         if curr_sum > n:
#             return

#         if i > n or i > 9:
#             return

#         if len(sol) > k:
#             return

#         #Don't Choose
#         backtrack(i+1, curr_sum)

#         #Choose
#         sol.append(i)
#         backtrack(i+1, curr_sum + i)
#         sol.pop()

#     backtrack(1, 0)
#     return res

# print(combinationSum3(2, 18))



def subsetsWithDup(nums):
    n = len(nums)
    nums = sorted(nums)
    res, sol = [], []

    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return

        # Don't Choose
        j = i
        while j+1 < n and nums[j] == nums[j+1]:
            j+=1
        backtrack(j+1)

        # Choose
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return res

print(subsetsWithDup([0]))        