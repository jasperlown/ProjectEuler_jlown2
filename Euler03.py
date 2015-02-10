# @author Jasper Lown (NetID: jlown2)

def findLargestPrime(number):
	largestFactor = 1
	for largestFactor in range(2,100000):
		while number % largestFactor == 0:
			number /= largestFactor
			if number == 1 or number == largestFactor:
				return largestFactor
	
print(findLargestPrime(600851475143))


