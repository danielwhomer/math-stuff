#This implementation of the fibonacci sequence uses 'memoization'
#known values are recorded in a dictionary and checked before new values are calcuated
#i.e. if we know fib(10), why calculate it again each time n > 10
#memoized calls cost constant time.
#the number of non-memoized calls is equal to n:
#fib(1), fib(2),...,fib(n)
#the non recursive work per call is constant
#the running time is therefore linear
import sys

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

print(fib(int(sys.argv[1])))
