class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return (self.x + other.x , self.y + other.y)

vec1 = Vector(3,4)
vec2 = Vector(5,6)
vec3 = vec1 + vec2
print("Addition of two vector", vec3)

class Student:
    def __init__(self, marks):
        self.marks = marks
    def __eq__(self, other):
        return self.marks == other.marks

student1 = Student(97)
student2 = Student(87)
print(student1 == student2)
