import sys
import math

#This function takes in a number n and returns a list of "True" or "False" from 2 to n where True = prime, False = not prime


def sieve_of_eratosthenes(n):
	multiples = []
	primes = []
	for i in range(2, n+1):
		if i not in multiples:
			primes.append(i)
			for j in range(i*i, n+1, i):
				multiples.append(j)
	return primes

s = sieve_of_eratosthenes(int(sys.argv[1]))

print(s)

		


