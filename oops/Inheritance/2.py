class Vehicle:
    def chasis(self):
        print("Chasis - I have iron chasis, helps in strong body and engine.")
    def engine(self):
        print("Engine - I'm the heart of a vehicle.")
    def tyres(self):
        print("Tyres - I'm the reason for the movement.")
class Car(Vehicle):
    def start(self):
        print("Car is starting..")
    def model(self):
        print("I'm a 2025 BMW M340i car")
    def mileage(self):
        print("I produce 10KMs per litre fuel.")
BMW = Car()
BMW.model()
BMW.mileage()
BMW.chasis()
BMW.engine()
BMW.tyres()
BMW.start()
