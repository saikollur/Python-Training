class Father:
    def show(self):
        print("This is Father's show() method")


class Mother:
    def show(self):
        print("This is Mother's show() method")


class Child(Father, Mother):
    pass

c = Child()
c.show()
print(Child.mro())
