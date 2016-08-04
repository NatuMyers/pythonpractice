def ana(str1,str2):

	
	if len(str1) != len(str2):
		return false
	

	hist = [26]


	for i in range(len(str1)):
		hist[i]+=1

	for i in range(len(str2)):
		if (hist[str2[i]]) == 0:
			return false
	return true


ana("test","etst")
