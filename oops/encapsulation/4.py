class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def area(self):
        a = self.__length * self.__width
        return a
    def perimeter(self):
        p = 2 * (self.__length + self.__width)
        return p

rec = Rectangle(10, 15)
print("Area of the Rectangle:", rec.area())
print("Perimeter of the Rectangle:", rec.perimeter())
