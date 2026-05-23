class BankAccount:
    def __init__(self):
        self.__AccountBalance = 0

    def deposit_money(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        
        self.__AccountBalance += amount

    def withdraw_money(self, amount):
        if amount > self.__AccountBalance:
            print("Insufficient Balance")
            return
        
        self.__AccountBalance -= amount

    def show_balance(self):
        print(f"Your Balance : {self.__AccountBalance}")

my_bank = BankAccount()
my_bank.deposit_money(1000)
amount_to_withdraw = int(input("Enter the Amount: "))
my_bank.withdraw_money(amount_to_withdraw)
my_bank.show_balance()