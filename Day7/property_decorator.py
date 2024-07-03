# class Student:
#     def __init__(self,Phy,Chem,Maths):
#         self.Phy = Phy
#         self.Chem = Chem
#         self.Math = Maths
#         self.percentage = str((self.Phy + self.Math+self.Chem)/3) + "%"
#
#     def calculatePercentage(self):
#         self.percentage = str((self.Phy + self.Math+self.Chem)/3) + "%"
#
#
# s1 = Student(99,97,99)
# print(s1.percentage)
#
# s1.Phy = 88
# s1.calculatePercentage()
# print(s1.percentage)


# Property decorator

class Student:
    def __init__(self,Phy,Chem,Maths):
        self.Phy = Phy
        self.Chem = Chem
        self.Math = Maths

    @property
    def percentage(self):
        return str((self.Phy + self.Math + self.Chem) / 3) + "%"



s1 = Student(99,97,99)
print(s1.percentage)

s1.Phy = 88
print(s1.percentage)