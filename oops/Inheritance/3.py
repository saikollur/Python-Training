class Shape:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

class Rectangle(Shape):
    def show(self):
        print("I'm Rectangle.")

    def area(self):
        area = self.length * self.breadth
        print("Area of a Rectangle:",area)
geo = Rectangle(10,12)
geo.show()
geo.area()
