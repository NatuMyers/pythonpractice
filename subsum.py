def subSum(arr):

	subsum = 0
	
	if len(arr) <= 0:
		return 0

	else:
		for i  in range(len(arr)):
			subsum += arr[i]
		return subsum + subSum(arr[1:]) + subSum(arr[:-1])


print (subSum([1,2,7]))
