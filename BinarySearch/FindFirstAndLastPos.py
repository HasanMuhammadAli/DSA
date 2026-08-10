class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        left = 0
        right = n-1
        flag = 0
        
        #Find First occurrence
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                ans = mid
                right = mid - 1
                flag = 1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            
        if not flag:
            return [-1, -1]
        else:
            ans = left
        
        #Find Last occurrence
        flag = 0
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                ans2 = mid
                left = mid+1
                flag =1
            else:
                right = mid-1
        
        if not flag:
            return [ans, ans]
        else:
            return [ans, ans2]
        

