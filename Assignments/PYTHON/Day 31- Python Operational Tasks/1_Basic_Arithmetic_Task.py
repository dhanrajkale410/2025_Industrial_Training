# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate sum
sum_result = num1 + num2
print(f"Sum: {sum_result}")

# Calculate difference
difference = num1 - num2
print(f"Difference: {difference}")

# Calculate product
product = num1 * num2
print(f"Product: {product}")

# Calculate division (handle divide by zero)
if num2 != 0:
    division = num1 / num2
    remainder = num1 % num2
    print(f"Division: {division}")
    print(f"Remainder: {remainder}")
else:
    print("Division by zero is not allowed.")

# Compare the two numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num2} is greater than {num1}.")
else:
    print("Both numbers are equal.")
