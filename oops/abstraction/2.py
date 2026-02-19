from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        return "Bike is starting.."
    def stop(self):
        return "Bike stopped."

class Car(Vehicle):
    def start(self):
        return "Car is starting.."
    def stop(self):
        return "Car stopped."

b = Bike()
c = Car()
print(b.start())
print(b.stop())
print(c.start())
print(c.stop())
