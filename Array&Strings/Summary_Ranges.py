'''
Name: Muhammad Ali Mosin Hasan
Date: 15/7/25
Problem: 228: Summary Ranges
'''

def summaryRanges(nums):
    ans = []
    i = 0

    while i < len(nums):
        start = nums[i]
        
        while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
            i += 1

        if start != nums[i]:
            ans.append(str(start) + '->' + str(nums[i]))
        else:
            ans.append(str(nums[i]))
        i += 1
    return ans
# Example usage and test cases for Summary_Ranges.py


print(summaryRanges([0,1,2,4,5,7]))      # Output: ['0->2', '4->5', '7']
print(summaryRanges([0,2,3,4,6,8,9]))    # Output: ['0', '2->4', '6', '8->9']
print(summaryRanges([]))                 # Output: []
print(summaryRanges([1]))                # Output: ['1']
print(summaryRanges([1,3]))              # Output: ['1', '3']
print(summaryRanges([-3,-2,-1,0,1]))     # Output: ['-3->1']