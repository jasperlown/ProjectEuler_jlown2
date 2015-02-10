# @author Jasper Lown (NetID: jlown2)

currentSum = 0

for i in range(1000):
	if i % 3 == 0:
		currentSum += i
	elif i % 5 == 0:
		currentSum += i

print(currentSum)