class Student:
    def __init__(self,fullname,marks):

        self.fullname = fullname
        self.marks = marks

    def welcome(self):
        print("welcome student",self.fullname)

    def get_marks(self):
        return self.marks

s1 = Student("DEV",97)
s1.welcome()
print(s1.get_marks())