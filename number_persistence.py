import sys

#https://en.wikipedia.org/wiki/Persistence_of_a_number

#Calculates the number of steps it takes to reduce a number down to a single digit by multiplying its digits
#For example when n = 39
#n = 3*9
#n = 2*7
#n = 1*4
#n = 4

#the current known most persistent number is 277777788888899 (11 steps)

def persistence(number, steps):
	if len(str(number)) == 1:
		return "DONE"
	digits = [int(i) for i in str(number)]

	result = 1
	for d in digits:
		result *= d
	print(result, steps)
	persistence(result, steps+1)
	

persistence(sys.argv[1], 1)
