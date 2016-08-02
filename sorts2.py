
def msort (arr):

	mid = len(arr)//2
	l = arr[0:mid]
	r = arr[mid:]
	
	if len(arr) <= 1:
		return arr

	if len(arr) > 1:
		msort(l)
		msort(r)


	i = 0
	j = 0
	k = 0

	while (i < len(l) and j < len(r)):

		if l[i] < r[j]:
			temp = l[i]
			l[i] = r[j]
			l[i] = temp
		else:
			temp = l
