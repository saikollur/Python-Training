from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

class Circle(Shape):
    pi = 3.14
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.pi * self.r**2

r = Rectangle(10,12)
c = Circle(4)

print("Area of rectangle :", r.area())
print("Area of circle    :", c.area())
