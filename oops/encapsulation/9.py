class VotingSystem:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def eligibility(self):
        if self.__age >= 18:
            print(f"{self.name} is eligible to vote.")
        else:
            print(f"{self.name} is NOT eligible to vote.")

    def display_age(self):
        print(f"{self.name}'s age is:", self.__age)

v1 = VotingSystem("Rahul", 20)
v2 = VotingSystem("Anu", 16)

v1.eligibility()
v2.eligibility()
