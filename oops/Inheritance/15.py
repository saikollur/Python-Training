class Parent:
    def show(self, name):
        print("Parent method called")
        print("Name:", name)

class Child(Parent):
    def show(self):
        print("Child method called")

c = Child()
c.show("Sai")
