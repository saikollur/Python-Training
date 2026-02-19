class Shape:
    def area(self):
        print("I calculate area.")
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print("Area of a Rectangle:",area)
s = Shape()
r = Rectangle(10,12)
s.area()
r.area()
