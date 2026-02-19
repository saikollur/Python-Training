class Book:
    def read(self):
        print("Reading a book..")

class Newspaper:
    def read(self):
        print("Reading a newspaper..")

def startReading(obj):
    obj.read()

startReading(Book())
startReading(Newspaper())
