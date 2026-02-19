class foodStall:
    def cook(self):
        print("Cooking started.")

    def process(self):
        print("Food is being prepared.")

class makeTea:
    def process(self):
        print("""Boil water in a pan.
Add tea leaves/powder and sugar.
Simmer for 2-3 minutes to release flavor.
Pour in milk and boil until it bubbles.
Strain into a cup""")


def pro(obj):
    obj.process()

pro(foodStall())
print("\n")
pro(makeTea())
