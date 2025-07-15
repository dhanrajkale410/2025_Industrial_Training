# Assignment 6: Dictionary Program
# Create a program that:
# Stores student names and their grades in a dictionary
# Allows adding new students
# Finds the average grade
# Identifies the top performer


students = {
    "Dhanraj" : 91,
    "Kunal" : 80,
    "Krushna" : 90,
    "Yugant" : 90
}

students["Gaurav"] = 86
students["Aditya"] = 85

total = sum(students.values())
count = len(students)
average = total / count

top_student = max(students, key=students.get)
top_grade = students[top_student]

print("Student Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

print(f"\nAverage Grade: {average:.2f}")
print(f"Top Performer: {top_student} with a grade of {top_grade}")
