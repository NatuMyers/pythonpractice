
#it
init = 1


itr = 20


n = 0

if (itr == 0):
	n = 0

elif(itr == 1):
	n = 1

else:
	while (init < itr):
		init = init + 2
		
		itr = itr - 1
		
	print init
