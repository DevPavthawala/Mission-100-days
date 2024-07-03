class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")


class ToyotaCar(car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("prius","electric")

print(car1.type) # throws error when super methord is not use and calling from parent class