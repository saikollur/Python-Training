class Father:
    def __init__(self, fname):
        self.fname = fname

    def showFather(self):
        print("Father Name:", self.fname)

class Mother:
    def __init__(self, mname):
        self.mname = mname

    def showMother(self):
        print("Mother Name:", self.mname)

class Child(Father, Mother):
    def __init__(self, fname, mname, cname):
        Father.__init__(self, fname)
        Mother.__init__(self, mname)
        self.cname = cname

    def showChild(self):
        print("Child Name:", self.cname)

c = Child("Ramesh", "Sita", "Rahul")

print()
c.showFather()
c.showMother()
c.showChild()
