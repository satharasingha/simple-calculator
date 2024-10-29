#Simple calculator

operator = input("Choose an operator (+ - * / ): ")
number1 = float(input("Enter you first number: "))
number2 = float(input("Enter you second number: "))

if operator == "+":
    result = number1 + number2
    print(round(result, 2))


elif operator == "-":
    result = number1 - number2
    print(round(result, 2))


elif operator == "*":
    result = number1 * number2
    print(round(result, 2))


elif operator == "/":
    result = number1 / number2
    print(round(result, 2))


else:
    print(f"{operator} is not valid operator")