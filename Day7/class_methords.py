# class Name:
#     name = "sitaram"
#
#     def changeName(self,name):
#         self.name = name
#
#
# p1 = Name()
# p1.changeName("ramesh")
# print(p1.name)
# print(Name.name)


# # to change name from  class
# class Name:
#     name = "sitaram"
#
#     def changeName(self,name):
#         # Name.name = name   # both are same
#         self.__class__.name = name
#
#
# p1 = Name()
# p1.changeName("ramesh")
# print(p1.name)
# print(Name.name)


# class methord

class Name:
    name = "sitaram"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Name()
p1.changename("Ramesh")
print(p1.name)
print(Name.name)

