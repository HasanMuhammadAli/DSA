#11. Container With Most Water
#Name: Muhammad Ali Hasan
#Date: 8/11/25
def max_area(heights):
	n = len(heights)
	l, r = 0, n	-1
	ans = 0
	while(l<r):
		area = min(heights[l], heights[r]) * (r-l)
		if heights[l] < heights[r]:
			l += 1
			ans = max(area, ans)
		elif heights[l] == heights[r]:
			ans = max(area, ans)
			l+=1 
			r-=1
		else:
			r-=1
			ans = max(area, ans)
	return ans

heights = [1,1]
max_parea = max_area(heights)
print(max_parea)