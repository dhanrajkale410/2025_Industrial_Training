# Assignment 5: Tuple Unpacking & Conversion
# Write a Python program that:
# Takes a tuple of (product, price, quantity)
# Unpacks it into separate variables
# Calculates total cost (price × quantity)
# Converts the tuple to a list to modify quantity
# Converts back to tuple and prints all values


# Create a tuple of (product, price, quantity)
product_info = ("Laptop", 50000, 2)

# Unpack the tuple into separate variables
product, price, quantity = product_info

# Calculate total cost (price × quantity)
total_cost = price * quantity

print(f"Product: {product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: {total_cost}")

# Convert the tuple to a list to modify quantity
product_list = list(product_info)
product_list[2] = 3  # Update quantity to 3

# Convert back to tuple
updated_product_info = tuple(product_list)

# Unpack and print updated values
product, price, quantity = updated_product_info
total_cost = price * quantity

print("\nAfter updating quantity:")
print(f"Product: {product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: {total_cost}")
