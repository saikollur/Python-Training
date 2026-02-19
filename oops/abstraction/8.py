class Student:
    def __init__(self, marks):
        self.marks = marks
    def __eq__(self, other):
        return self.marks == other.marks
st1 = Student(95)
st2 = Student(95)
print(st1 == st2)
