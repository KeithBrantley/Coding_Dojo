class BankAccount:
    def __init__(self, Name, Int_rate = 0.01, Balance = 0):
        self.name = Name
        self.int_rate = Int_rate
        self.balance = Balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        # self.balance -= amount
        if(self.balance <= amount):
            print("Insufficiant funds: Charging a $5 fee.")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        print(self.name + " Balance is " + "$" + str(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

first_account = BankAccount("Checking")

second_account = BankAccount("Savings")

first_account.deposit(50).deposit(70).deposit(300).withdrawal(200).yield_interest().display_account_info()

second_account.deposit(100).deposit(100).withdrawal(50).withdrawal(60).withdrawal(600).withdrawal(98).yield_interest().display_account_info()



