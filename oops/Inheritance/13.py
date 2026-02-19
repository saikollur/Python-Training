class Parent:
    def play(self):
        print("Parent class - I play cricket.")

class child(Parent):
    def play(self):
        print("Child class - I don't play cricket.")
        super().play()
c = child()
c.play()
