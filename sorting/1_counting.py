from collections import Counter
def sortByBits(arr):
    sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted_arr

arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))