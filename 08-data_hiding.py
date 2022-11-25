from random import randint


class BankAccount:
    def __new__(cls, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, balance):
        self.__balance = balance  # private -> priv8
        self._key = randint(100, 999)  # protect
        self.name = name

    def get_balance(self):
        return self.__balance

    def __repr__(self):
        return f"<{self.name.title()}: {self.__balance}>"


ali_acc = BankAccount('ali yazdani', 20000)

# print(ali_acc._BankAccount__balance)
print(ali_acc)

"""

Bank
-> Saderat
-> Sepah

Account:
--> save in file | validation
--> profile -> composite
--> validation
--> + - len

reza_acc = Account 
# Account.register() || @classmethod


"""
