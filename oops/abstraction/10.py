from datetime import time
class Time:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return list((self.x + other.x, self.y + other.y))
tm1 = Time(10,30)
tm2 = Time(5,15)
tm3 = tm1 + tm2
if tm3[0] > 12:
    tm3[0] -= 12
print(f'Time is {tm3[0]}:{tm3[1]}')
