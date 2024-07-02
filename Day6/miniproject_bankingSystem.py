
# banking

class Account:

    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print(f"Rs {amount} debited ")
        print(f"Your balance is {self.get_balance()}")

    def creit(self,amount):
        self.balance += amount
        print(f"Rs {amount} creadited")
        print(f"Your balance is {self.get_balance()}")

    def get_balance(self):
        return self.balance

user1 = Account(10000,12234567)
user1.debit(1000)
user1.creit(2000)
user1.creit(40000)