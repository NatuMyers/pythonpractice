def hashfunc(key):

	for char in key:
		hash+= ord(char)
	hash%=5
	return hash



class HashMap:

	def __init__(self):
		self.size = 6
		self.map = [None] * self.size


	
