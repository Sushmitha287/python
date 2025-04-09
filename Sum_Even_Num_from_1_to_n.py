#Summing Even Numbers from 1 to n
number = int(input("Enter a number:"))
sum1 = 0
for i in range(1, number):
	if i % 2 == 0:
		sum1 = sum1 + i
print('Sum of even number from 1 to n is ', sum1)