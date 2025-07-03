'''
Name: Muhammad Ali Mosin Hasan
Date: 3/6/25
Problem: 84: Largest Rectangle in Histogram
'''

def largestRectangleArea(heights):
    '''
    Calculates the area of the largest rectangle that can be formed in a histogram.

    The function takes a list of integers representing the heights of histogram bars,
    and returns the maximum rectangular area that can be formed using consecutive bars.
    '''
    n = len( heights )
    stk = []
    max_area = 0

    for i, height in enumerate( heights ): 
        start = i
        while stk and height < stk[-1][0]:
            h, j = stk.pop()
            w = i - j
            a = h * w
            max_area = max( max_area, a)
            start = j
        stk.append((height, start))
    
    while stk:
        h, j = stk.pop()
        w = n - j
        max_area = max(max_area, h*w)

    return max_area


heights = [2,1,5,6,2,3]
print("Test Case 1:")
print(largestRectangleArea(heights))
print()

heights = [2,4]
print("Test Case 2:")
print(largestRectangleArea(heights))
print()
