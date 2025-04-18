#How to find the Numbers Divisible by Another Number in Python

list1 = list(map(int, input("Enter list of numbers:").split()))
div_num = int(input("Enter a divisor number:"))
list2 = []

for n in list1:
	if n % div_num == 0:
		list2.append(n)
print("Numbers divisiable by",div_num, "are :", list2)