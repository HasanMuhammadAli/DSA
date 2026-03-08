def twoSum(arr, target):
    left, right = 0, len(arr) - 1
    sum = 0
    while left < right:
        sum = arr[left] + arr[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return left, right

arr = [0, 1, 3, 5]
target = 6
print("The nums found on index: ",twoSum(arr, target))