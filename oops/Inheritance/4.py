class Animal:
    def breathe(self):
        print("Breathing")
class Dog(Animal):
    def bark(self):
        print("Barking")
class Puppy(Dog):
    def walk(self):
        print("Walking")
p = Puppy()
p.breathe()
p.bark()
p.walk()
