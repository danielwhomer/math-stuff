import sys
import math

def sieve(n):
	A = []
	for x in range(2, n+1):
		A.append(True)

	for i in range(2, int(math.sqrt(n)), 2):	
		if A[x-2] is True:
			for j in range(i**2, n, i):
				A[j-2] = False
	return A


print(sieve(argv[1]))


