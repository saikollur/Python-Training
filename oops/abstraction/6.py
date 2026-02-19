class point1():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x), (self.y + other.y)

p1 = point1(4,5)
p2 = point1(2,5)    
p3 = p1 + p2
print(p3)
