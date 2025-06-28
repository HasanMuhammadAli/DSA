'''
Name: Muhammad Ali Mosin Hasan
Date: 28/6/25
Problem: 1207: Unique Number of Occurrences
'''

from collections import Counter


def  isUniqueOccurrence(arr):
    
    count = Counter(arr)
    freq_arr = []
    for freq in count.values():
        freq_arr.append(freq)
    freq_arr.sort()
    
    for i in range(len(freq_arr)-1):
        if freq_arr[i] == freq_arr[i+1]:
            return False
    return True
    
    '''
    count = Counter(arr)
    freq_arr = list(count.values())
    freq_arr.sort()
    for i in range(len(freq_arr)-1):
        if freq_arr[i] == freq_arr[i+1]:
            return False
    return True
    '''

arr = [1,2,2,1,1,3]
result = isUniqueOccurrence(arr)
print(result)

arr = [1,2]
result = isUniqueOccurrence(arr)
print(result)