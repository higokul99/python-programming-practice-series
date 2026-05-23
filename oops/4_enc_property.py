class Bank:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid")
        else:
            self.__balance = amount

b = Bank()
b.balance = 1000
print(b.balance)