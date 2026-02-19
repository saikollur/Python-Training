class Actor:
    def __init__(self, name):
        self.name = name
        print("Parent Constructor Called")

class Hero(Actor):
    def __init__(self, name, industry):
        super().__init__(name)
        self.industry = industry
        print("Hero constructor called.")

class starHero(Hero):
    def __init__(self, name, industry, fans):
        super().__init__(name, industry)
        self.fans = fans
        print("starHero constructor called.")

    def display(self):
        print("\nActor Name  :", self.name)
        print("Industry    :", self.industry)
        print("Fan Base    :", self.fans)

ac = starHero("Pawan Kalyan", "Tollywood", "Cult following")
ac.display()
