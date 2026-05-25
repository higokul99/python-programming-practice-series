class Parent:
    def __init__(self):
        self.__account_balance = 10000000

    def get_account_balance(self):
        return self.__account_balance

class Child(Parent):
    def show(self):
        print(self.__account_balance)

c = Child()
print(c.get_account_balance())