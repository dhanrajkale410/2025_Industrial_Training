# Task 1: Polymorphism / Overriding
# 1. Create a base class Shape with a method area() that returns 0.
# * Create child classes Circle and Rectangle that override the area() method:
#       Circle should use πr² (use math.pi).
#       Rectangle should use length × width.
# * Create a list of shapes and call the area() method in a loop to demonstrate polymorphism.

import math

class Shape :
    def area(self) :
        return 0

class Circle :
    def __init__(self,radius):
        self.radius = radius

    def area(self) :
        return math.pi*self.radius**2
        

class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self) :
        return self.length*self.width
    

shapes = [
    Circle(5),
    Rectangle(6,9)
]

for shape in shapes :
    print(f"Area : {shape.area()}")
    