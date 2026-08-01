def maxArea(height):
    n = len(height)
    l = 0
    r = n-1
    max_area = 0
    while l < r:
        minn_height = min(height[l], height[r])
        area = minn_height * (r-l)
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
height = [1,1]
print(maxArea(height))
        