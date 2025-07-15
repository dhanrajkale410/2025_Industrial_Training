#Create a program that: Creates a tuple of 5 student names,Prints the second student's name,Checks if "Alice" is in the tuple,Concatenates with another tuple of 3 new students,Prints the length of the final tuple

students = ("Dhanraj", "Kunal", "Uday", "Aditya", "Ganesh")

print("Second student's name:", students[1])

if "Alice" in students:
    print("Alice is in the tuple.")
else:
    print("Alice is not in the tuple.")

new_students = ("Alice", "Robert", "James")
all_students = students + new_students

print("Length of final tuple:", len(all_students))