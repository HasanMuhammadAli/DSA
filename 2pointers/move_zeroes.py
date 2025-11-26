#283. Move Zeroes
#Name: Muhammad Ali Hasan
#Date: 07/11/25
def move_zeroes(nums):
	l, r = 0, 0
	n = len(nums)
	while (r <= n-1):
		if nums[r] != 0 and nums[l] != 0:
			r += 1
			l += 1
		elif nums[r] == 0 and nums[l] == 0:
			r += 1
		elif nums[r] != 0 and nums[l] == 0:
			nums[r], nums[l] = nums[l], nums[r]
			r += 1
			l += 1
	return nums

nums = [4,2,4,0,0,3,0,5,1,0]
nums = move_zeroes(nums)
print(nums)