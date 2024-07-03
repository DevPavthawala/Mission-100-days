class employ:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetail(self):
        print(f"Role : {self.role}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")

class engineer(employ):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT" , "75000")

E1 = employ("senior Dev","IT","50000")
E1.showDetail()

eng1 = engineer("Dev",21)
eng1.showDetail()