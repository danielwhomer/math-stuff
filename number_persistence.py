import sys

def persistence(number, steps):
	if len(str(number)) == 1:
		print(number)
		return "DONE"
	digits = [int(i) for i in str(number)]

	result = 1
	for d in digits:
		result *= d
	print(result, steps)
	persistence(result, steps+1)
	

persistence(sys.argv[1], 1)
