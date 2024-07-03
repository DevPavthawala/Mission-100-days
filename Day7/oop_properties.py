class Student:

    def __init__(self,name):
        self.name= name

s1 = Student("Dev")
print(s1.name)

;
del s1.name # can del attribute
del s1 # can del object
print(s1)
