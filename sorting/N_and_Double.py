def checkIfExist(arr):
    arr.sort()
    n = len(arr)

    i, j = 0, 1

    while j < n and i < n:
        if i == j:
            j += 1
            continue

        if arr[j] == 2 * arr[i]:
            return True
        elif arr[j] < 2 * arr[i]:
            j += 1
        else:
            i += 1

    return False

arr = [10,2,5,3]
print(checkIfExist(arr))
arr = [3,1,7,11]
print(checkIfExist(arr))