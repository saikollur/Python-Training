class University:
    def process(self):
        print("University Registration Process:")
        print("Click on apply to register.")
        print("Click on the course you need to enroll.")
        print("Fill out all the detail.")
        print("Pay the application fee.")
        print("Applied successfully")

class OnlineShopping:
    def process(self):
        print("\nShopping Process:")
        print("Select product")
        print("Add to cart")
        print("Enter address")
        print("Make payment")
        print("Order placed successfully")

class Bank:
    def process(self):
        print("\nBank Loan Process:")
        print("Submit documents")
        print("Verification")
        print("Approval")
        print("Loan credited")

def startProcess(obj):
    obj.process()

u = University()
s = OnlineShopping()
b = Bank()

startProcess(u)
startProcess(s)
startProcess(b)
