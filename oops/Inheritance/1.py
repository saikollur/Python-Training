class Person:
    def show(self):
        print("I'm a person")
class Student(Person):
    def college(self):
        print("Also a student and I go to college everyday.")
a = Student()
a.show()
a.college()
