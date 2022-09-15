factorial = 1
num1 = input("Enter first number: ")
op = input("Enter operator: ")
if op == "!":
    if int(num1) < 0:
        print("Error! Can't do factorial for negative numbers")
    elif int(num1) == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, int(num1) + 1):
            factorial = factorial * i
        print("Result = " + str(factorial))
    quit()

num2 = input("Enter second number: ")

if op == "+" :
    result = float(num1) + float(num2)
elif op == "-" :
    result = float(num1) - float(num2)
elif op == "/" :
    result = float(num1) / float(num2)
elif op == "*":
    result = float(num1) * float(num2)
else :
    print("Error! Invalid operator")

print("Result = " + str(result))