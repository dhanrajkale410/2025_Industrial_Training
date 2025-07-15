# Task 3: Method Implementation
# Objective: Enhance the Student class with additional functionality.

# Add these methods to your Student class:
# - add_credits(course_name, credits): Store credit hours for each course
# - calculate_weighted_gpa(): Calculate GPA weighted by credit hours
# - get_highest_grade(): Returns the course name and highest grade
# - _str_: Returns a string representation of the student

# Task 3: Enhanced Student Class with More Methods

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}   # { course_name: grade }
        self.credits = {}   # { course_name: credits }

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

    def add_credits(self, course_name, credits):
        if course_name in self.courses:
            self.credits[course_name] = credits
            print(f"Added {credits} credit hours for {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def calculate_gpa(self):
        grades = [grade for grade in self.courses.values() if grade is not None]
        if grades:
            gpa = sum(grades) / len(grades)
            return round(gpa, 2)
        else:
            return 0.0

    def calculate_weighted_gpa(self):
        total_points = 0
        total_credits = 0
        for course, grade in self.courses.items():
            if grade is not None and course in self.credits:
                total_points += grade * self.credits[course]
                total_credits += self.credits[course]
        if total_credits == 0:
            return 0.0
        else:
            return round(total_points / total_credits, 2)

    def get_highest_grade(self):
        valid_grades = {course: grade for course, grade in self.courses.items() if grade is not None}
        if valid_grades:
            highest_course = max(valid_grades, key=valid_grades.get)
            return (highest_course, valid_grades[highest_course])
        else:
            return (None, None)

    def display_info(self):
        print(f"\n{self}")
        print("Courses, Grades, and Credits:")
        for course in self.courses:
            grade = self.courses[course]
            credits = self.credits.get(course, "N/A")
            print(f"  {course}: Grade={grade}, Credits={credits}")
        print(f"GPA: {self.calculate_gpa()}")
        print(f"Weighted GPA: {self.calculate_weighted_gpa()}")
        highest = self.get_highest_grade()
        if highest[0]:
            print(f"Highest Grade: {highest[1]} in {highest[0]}")
        else:
            print("No grades yet!")

    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.student_id}"


# === Using the enhanced class ===

student1 = Student("Dhanraj", 31)
student2 = Student("Kunal", 24)

# Enroll in courses
student1.enroll("Java")
student1.enroll("Python")

student2.enroll("C++")
student2.enroll("C")

# Add credits
student1.add_credits("Java", 3)
student1.add_credits("Python", 4)

student2.add_credits("C++", 3)
student2.add_credits("C", 2)

# Update grades
student1.update_grade("Java", 85)
student1.update_grade("Python", 90)

student2.update_grade("C++", 78)
student2.update_grade("C", 88)

# Display all info
student1.display_info()
student2.display_info()
