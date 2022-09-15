int_or_float = input("1.integer\t2.float\nEnter whether you want to add integer numbers or float numbers: ")
num1 = input("Enter first number: ")
op = input("Enter operator: ")
num2 = input("Enter second number: ")


if int_or_float == "1":
    if op == "+":
        result = int(num1) + int(num2)
    elif op == "-":
        result = int(num1) - int(num2)
    else :
        print("Error! Invalid operator")


if int_or_float == "2":
    if op == "+":
        result = float(num1) + float(num2)
    elif op == "-":
        result = float(num1) - float(num2)
    else :
        print("Error! Invalid operator")

print("The result = " + str(result))

