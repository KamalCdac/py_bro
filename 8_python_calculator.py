# Python Calculator

operator = input("Enter an Operator? (+, -, *, /): ")

num1 = float(input("Enter the 1st number"))
num2 = float(input("Enter the 2nd number"))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not valid operator")

