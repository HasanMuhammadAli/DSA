def mostTrapping(heights):
    if not heights: return 0
    left, right = 0, len(heights)-1
    left_max, right_max = heights[left], heights[right]
    res = 0


    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            res += left_max - heights[left]
        
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            res += right_max - heights[right]

    return res

heights = []
print(mostTrapping(heights))

heights = [4]
print(mostTrapping(heights))

heights = [3, 5]
print(mostTrapping(heights))

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(mostTrapping(heights))
