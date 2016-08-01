#Given a list of strings, return all pairs of strings that can make a palindrome.  


def pal(lis):

	pals = []

	#base case empty

	if len(lis) <=1:
		return 0
	

	else: # real deal
	
		for i in range(len(lis)):

			for j in range(len(lis)):
				
				#if (true): 

				if (lis[i] + lis[j] == lis[j] + lis[i]):

					pals.append( lis[i] + lis[j] )


	print (pals)
	


pal(["abc", "cba"])
