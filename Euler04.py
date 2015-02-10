# @author Jasper Lown (NetID: jlown2)

def isPalindrome(number):
	return str(number) == str(number)[::-1]
	
product = 0	

for i in range(100, 999, 1):
	for j in range(100, 999, 1):
		if isPalindrome(i*j) and i*j > product:
			product = i*j
			
print(product)
		