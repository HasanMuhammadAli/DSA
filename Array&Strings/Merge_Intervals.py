'''
Name: Muhammad Ali Mosin Hasan
Date: 17/7/25
Problem: 56: Merge Intervals
'''

def merge(intervals):      
    '''
    Merges overlapping intervals.
    '''
    intervals.sort(key = lambda interval: interval[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        else: 
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected: [[1,6],[8,10],[15,18]]
print(merge([[1,2],[3,4],[5,6]]))  # Expected: [[1,2],[3,4],[5,6]]
print(merge([[1,4],[2,5],[3,6]]))  # Expected: [[1,6]]
