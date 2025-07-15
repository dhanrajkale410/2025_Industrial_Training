"""
Assignment 3: String Methods
1. Write a program that combines a user's first and last name with a space in between.

2. Create a formatted string that displays: "The price of [item] is $[price]" (use variables).

3. Convert the string "hello world" to "HELLO WORLD" using string methods.

4. Use .join() to convert the list ['Python', 'is', 'awesome'] into a proper sentence.

5. Print today's date in "DD-MM-YYYY" format using string formatting (use datetime module).
"""

# 1. Write a program that combines a user's first and last name with a space in between.

def formattedName(fName,lName) :
    fullName = fName + " " + lName
    return fullName

firstName = input("Enter First Name : ")
lastName = input("Enter Last Name : ")
print("Full Name : ",(formattedName(firstName,lastName)))


# 2. Create a formatted string that displays: "The price of [item] is $[price]" (use variables).

item = input("Enter Item Name : ")
price = float(input("Enter Item Price : "))

print(f"The Price of {item} is {price}")

# 3. Convert the string "hello world" to "HELLO WORLD" using string methods.

str = "hello world"
print(str.upper())


# 4. Use .join() to convert the list ['Python', 'is', 'awesome'] into a proper sentence.

list1 = ["Python","is"]
list2 = ["Awesome"]
print(" ".join(list1) + " " + list2[0])

# 5. Print today's date in "DD-MM-YYYY" format using string formatting (use datetime module).
import datetime

x = datetime.datetime.now()

print(x.strftime("%x"))