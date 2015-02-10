# @author Jasper Lown (NetID: jlown2)

def isDivisible(number):
	for i in range(3,20,1):
		if number % i != 0:
			return False
		else:
			continue
	return True

smallestProduct = 2520
while not isDivisible(smallestProduct):
	smallestProduct += 2520
	
print(smallestProduct)