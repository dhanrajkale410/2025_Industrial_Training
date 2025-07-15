# Simple Calculator using if-else

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Choose operation: +, -, *, /")
operator = input("Enter operator: ")

if operator == '+':
    result = num1 + num2
    print(f"Result: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator. Please choose +, -, *, or /.")