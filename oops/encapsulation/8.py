class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def discount(self, percent):
        if percent < 0 or percent > 100:
            print("Invalid discount percentage!")
            return

        finalAmount = (percent / 100) * self.__price
        self.__price -= finalAmount
        print(f"{percent}% discount applied.")

    def displayPrice(self):
        print(f"Price of {self.name}: ₹{self.__price:.2f}")



p1 = Product("Headphones", 2000)

p1.displayPrice()
p1.discount(10)
p1.displayPrice()
p1.discount(150)
p1.displayPrice()
