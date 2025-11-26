def maxAverage(nums, k):
	n = len(nums)
	curr_sum = 0
	max_sum = -999999
	for i in range(k):
		curr_sum += nums[i]
	max_sum = curr_sum
	for i in range(k,n):
		curr_sum = curr_sum + nums[i] - nums[i-k]
		max_sum = max(max_sum, curr_sum)
	return max_sum/k
	





nums = [1,12,-5,-6,50,3]
k = 4
print(maxAverage(nums, k))
