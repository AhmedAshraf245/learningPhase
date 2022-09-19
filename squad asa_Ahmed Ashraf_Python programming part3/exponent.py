#I added a negative_exponent_calculator to deal with negative powers since the normal function
#will only work with positive powers

def exponent_calculator(number, power):
    result = 1
    for i in range(power, 0, -1):
        result = result * number
    return result


def negative_exponent_calculator(number, power):
    result = 1
    for i in range(0, power, -1):
        result = result / number
    return result


def exponent_calculator_built_in(number, power):
    return pow(number, power)


user_number = input("Enter the number: ")
user_exponent = input("Enter the exponent: ")

if int(user_exponent) < 0:
    print("Result WITHOUT built-in function: " + str(negative_exponent_calculator(int(user_number), int(user_exponent))))
else:
    print("Result WITHOUT built-in function: " + str(exponent_calculator(int(user_number), int(user_exponent))))

print("Result WITH built-in function: " + str(exponent_calculator_built_in(int(user_number), int(user_exponent))))