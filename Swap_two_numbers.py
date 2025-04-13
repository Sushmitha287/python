#Swap two numbers using Temporary Variable

a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
print("Before swapping :", a, b)
temp = a
a = b
b = temp

print("After swapping :",a, b)