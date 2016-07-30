

def rev(str,reverse=""):

	if len(str) < 1:
		return (str)

	else:
		reverse=reverse+str[-1]
		return (  rev(str[:-1],reverse)   )



a="toronto"
#print(a[:-1])
print(rev(a))
