class ArtClass:
    def draw(self):
        print("I'm drawing in my artclass.")
        
class Person:
    def draw(self):
        print("I draw human faces.")

def duckTyping(fun):
    fun.draw()

duckTyping(ArtClass())
duckTyping(Person())
