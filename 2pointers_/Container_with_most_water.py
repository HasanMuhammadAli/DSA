def mostWater(heights):
    left, right = 0, len(heights)-1
    max_area = 0
    while left < right:
        area = (right-left) * min(heights[left], heights[right])
        max_area = max(area, max_area)
        if heights[left] <  heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

heights = [1, 3, 5, 4]
print(mostWater(heights))
