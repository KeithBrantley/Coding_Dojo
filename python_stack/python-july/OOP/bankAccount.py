class BankAccount:
    def __init__(self, int_rate = 0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        if(self.balance < 0):
            print("Insufficiant Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance is ${self.balance}.")
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

account1 = BankAccount().deposit(100).deposit(100).deposit(100).withdrawal(50).display_account_info()
account2 = BankAccount().deposit(200).deposit(200).withdrawal(200).withdrawal(100).withdrawal(100).withdrawal(100).display_account_info()

