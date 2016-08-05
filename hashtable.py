table = [None]*10

def hashFunc():
	
	return x%10


def insert(table,key,val):

	table[hashFunc(key)] = val



print (table)

insert(table,"a",5)
