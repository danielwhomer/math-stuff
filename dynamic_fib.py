#This implementation of the fibonacci sequence uses 'memoization'
#known values are recorded in a dictionary and checked before new values are calcuated
#i.e. if we know fib(10), why calculate it again each time n > 10

memo = {}

def fib(n):
	if n in memo: 
		return memo[n]
	if n <= 2: 
		f = 1
	else: 
		f = fib(n-1)+fib(n-2)
	memo[n] = f
	return f

print(fib(6))
