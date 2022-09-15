num1 = input("Enter first number: ")
op = input("Enter operator: ")
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