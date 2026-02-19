class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return (self.x - other.x),(self.y - other.y)
vec1 = Vector(5,3)
vec2 = Vector(2,1)
print(vec1 - vec2)



