class User:
    def __init__(self, password):
        self.__password = password
    def updatePassword(self,newPassword):
        self.__password = newPassword
    def verifyPassword(self,pw):
        if self.__password == pw:
            print("Correct password!")
        else:
            print("Incorrect Password")
user = User("saikollur")
newPassword = input()
user.updatePassword(newPassword)
user.verifyPassword(newPassword)
