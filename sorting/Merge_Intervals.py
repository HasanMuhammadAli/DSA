def merge(intervals):
        intervals.sort()
        i = 0
        ans = []

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            j = i+1
            while j<len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            
            ans.append([start, end])
            i = j

        
        return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))