class Student:
    college_name = "ABC college" # store only one time in memory( use when all have same values then no need to store induividual, it increase space)
    # default Constructor (created by Python if we dont write)
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self,fullname,hobbies):
        self.fullname = fullname
        self.hobbies = hobbies
        print("Creating new student in database")

s1 = Student("Karan","Swimming")
print(s1.fullname,s1.hobbies)

print(Student.college_name)