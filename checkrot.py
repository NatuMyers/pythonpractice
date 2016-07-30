arr1=[1,2,3,5,6,7,8]
arr2=[5,6,7,8,1,2,3]
arr3=[4,4,4,4,4,4,4]
arr4=[3]


#shortcuts/base cases

#avg case
matches = 0
indivCorresp = 0
for i in range(len(arr1)):
	for j in range(len(arr2)):
		if arr1[i] == arr2[j]:
			indivCorresp = indivCorresp+1
		if  indivCorresp == 1:
			matches = matches + 1
		indivCorresp = 0	
if matches == len(arr1):
	print("this is a rot!")
else:
	print("this is not a rot!")
	
