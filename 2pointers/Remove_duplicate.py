def removeDuplicates(nums):
        
        if not nums:
                return 0
        i = 0
        j = 1
        count = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                   count += 1
                   i += 1
                   j += 1

            else:
                   i += 1
                   j += 1

        return count
print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1]))

         