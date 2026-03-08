def twoSum(numbers, target):
    n = len(numbers)
    l = 0
    r = n-1
    
    while l < r:
        summ = numbers[l] + numbers[r]
        if summ == target:
            return [l+1, r+1]
        elif summ < target:
            l += 1
        elif summ > target:
            r -= 1
    

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))