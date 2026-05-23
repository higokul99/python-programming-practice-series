class ATM:

    def __init__(self):
        self.__pin = 1234
        self.__balance = 5400

    def check_pin(self, pin):
        return pin == self.__pin

    def deposit(self, pin, amount):
        
        if self.check_pin(pin):
            self.__balance += amount
        else:
            print("Wrong PIN")
            return

    def withdraw(self, pin, amount):
        if not self.check_pin(pin):
            print("Wrong PIN")
            return 
        
        if amount > self.__balance:
            print("Insufficient Balance!")
            return 
        
        self.__balance -= amount
        print("Transaction completed!")

    def check_balance(self, pin):
        if not self.check_pin(pin):
            print("Wrong PIN")
            return
        
        print("Your Balance :",self.__balance)
        return
    

atm = ATM()
atm.withdraw(1234, 500)
atm.deposit(1234, 20000000)
atm.check_balance(1234)