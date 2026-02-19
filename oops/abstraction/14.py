class Car:
    def move(self):
        print("Car is moving..")
class Bike:
    def move(self):
        print("Bike is moving..")
def makeThemMove(obj):
    obj.move()

for _ in range(5):
    makeThemMove(Car())
    makeThemMove(Bike())
