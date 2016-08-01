
# fib naive is naive because its exponential time
# and recalcs stuff

def fibnaive(n):
	if (n <= 1):
		return n
	else:
		return fib(n-1)+fib(n-2)

print(fibnaive(5))


# simple map object, m, which maps each value of fib that has already been calculated to its result, and we modify our function to use it and update it.
