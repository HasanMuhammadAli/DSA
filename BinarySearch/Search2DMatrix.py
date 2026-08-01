def searchMatrix(matrix, target):
    #Time:O(log(m*n))
    #Space:O(1)
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    t = m*n
    right = t-1

    while left <= right:
        mid = left + ((right-left)//2)
        i = mid // n
        j = mid %n
        mid_val = matrix[i][j]

        if target == mid_val:
            return True
        elif target < mid_val:
            right = mid-1
        else:
            left = mid+1

    return False   

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))