arr = [2,2,2,2,4,5,2,45,3,4,4]

mostFrq = 0
mostFrqAmount = 0

for i in range(len(arr)):

        amountOfCurrent = 0
	
        # now look at temp element
        for j in range(len(arr)):
                if (arr[j] == arr[i]):
			amountOfCurrent = amountOfCurrent + 1

	if (amountOfCurrent > mostFrqAmount):
		mostFrqAmount = amountOfCurrent
		mostFrq = arr[i]
	
print(mostFrq)
print(mostFrqAmount)

#for i in arr:

#	current = arr[i]
#	amountOfCurrent = 0

	# now look at temp element
#	for j in arr:
#		if arr[j] = current
		

