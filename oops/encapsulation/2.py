class Student:
    def __init__(self):
        self.__marks = 0

    def setMarks(self, studentMarks):
        self.__marks = studentMarks

    def getMarks(self):
        return self.__marks


st = Student()
st.setMarks(98)
print("Student Marks:",st.getMarks())
