class Number:
    def __init__(self, x):
        self.x = x
    def __mul__(self,other):
        return self.x * other.x
num1 = Number(2)
num2 = Number(6)
multiply = num1 * num2
print(multiply)
