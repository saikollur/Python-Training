class Dog:
    def sound(self):
        print("Dog Barks")
class Cat:
    def sound(self):
        print("Cat meows")
class Cow:
    def sound(self):
        print("Cow moos")

def sounds(animal):
    animal.sound()

sounds(Dog())
sounds(Cat())
sounds(Cow())
