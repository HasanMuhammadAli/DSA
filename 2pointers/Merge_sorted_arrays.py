#88. Merge Sorted Arrays
#Name : Muhammad Ali Mosin Hasan
#Date: 09/11/25

def merge(n1, m, n2, n):
	l = m-1
	r = n-1
	k = m+n-1
	while r >= 0:
		if l >=0 and n1[l] > n2[r]:
			n1[k] = n1[l]
			l -= 1
		else:
			n1[k] = n2[r]
			r -= 1
		k -= 1
			
	return n1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ans = merge(nums1, m, nums2, n)
print(ans)