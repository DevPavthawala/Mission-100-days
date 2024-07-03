# usign __gt__ function make greater than in item price


class order:
    def __init__(self,item,price):
        self.items = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


ord1 = order("chips",20)
ord2 = order("coke",40)

print(ord1 > ord2)
print(ord1 < ord2)