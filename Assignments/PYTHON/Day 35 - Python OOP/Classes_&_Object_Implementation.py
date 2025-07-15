# Task 2: Class and Object Implementation 

# Create a Student class to manage student information.
# Create a Student class with:
# Attributes: name, student_id, courses (dictionary to store course names and grades)
# Methods:
# enroll(course_name): Adds a course with default grade None
# update_grade(course_name, grade): Updates grade for a course
# calculate_gpa(): Returns average of all grades (ignore None values)
# display_info(): Shows all student information
# Create at least two Student objects and demonstrate all methods

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # Dictionary to store course names and grades

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None
            print(f"{self.name} has enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Updated grade for {course_name} to {grade}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def calculate_gpa(self):
        grades = [grade for grade in self.courses.values() if grade is not None]
        if grades:
            gpa = sum(grades) / len(grades)
            return round(gpa, 2)
        else:
            return 0.0

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            print(f"  {course}: {grade}")
        print(f"GPA: {self.calculate_gpa()}")


# Create two Student objects
student1 = Student("Dhanraj", 31)
student2 = Student("Kunal", 24)

# Enroll in courses
student1.enroll("Java")
student1.enroll("Python")

student2.enroll("C++")
student2.enroll("C")

# Update grades
student1.update_grade("Java", 85)
student1.update_grade("Python", 90)

student2.update_grade("C++", 78)
student2.update_grade("C", 88)

# Display info
student1.display_info()
student2.display_info()
