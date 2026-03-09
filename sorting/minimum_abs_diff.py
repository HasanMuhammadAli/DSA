def minimumAbsDifference(arr):
    arr.sort()
    ans = []
    min_diff = float('inf')

    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]

        if diff < min_diff:
            min_diff = diff
            ans = [[arr[i], arr[i+1]]]
        elif diff == min_diff:
            ans.append([arr[i], arr[i+1]])

    return ans

arr = [4,2,1,3]
print(minimumAbsDifference(arr))
arr = [1,3,6,10,15]
print(minimumAbsDifference(arr))
arr = [3,8,-10,23,19,-4,-14,27]
print(minimumAbsDifference(arr))