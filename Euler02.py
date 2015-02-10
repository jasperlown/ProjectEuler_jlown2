# @author Jasper Lown (NetID: jlown2)

currentSum = 0
fib = [1,1,0]

while fib[1] < 4000000:
	if fib[1] % 2 == 0:
		currentSum += fib[1]
	fib[2] = fib[0]+fib[1]
	fib[0] = fib[1]
	fib[1] = fib[2]
	
print(currentSum)