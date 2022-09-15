num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

sum1 = float(num1) + float(num2) + float(num3)
avg1 = sum1 / 3
print("Sum = " + str(sum1))
print("Average = " + str(avg1))



#Another method using built-in functions:

numbers = [float(num1), float(num2), float(num3)]
sum2 = sum(numbers)
avg2 = sum2 / len(numbers)
print("Sum = " + str(sum2))
print("Average = " + str(avg2))