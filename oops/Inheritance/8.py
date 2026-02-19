class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle:", area)

c = Circle("Circle", 7)
t = Triangle("Triangle", 10, 5)

c.area()
t.area()
