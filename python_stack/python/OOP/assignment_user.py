class BankAccount:
    def __init__(self, Int_rate = 0.02, Balance = 0):
        self.int_rate = Int_rate
        self.balance = Balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        # self.balance -= amount
        if(self.balance < amount):
            print("Insufficiant funds: Charging a $5 fee.")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        print(self.balance) 
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, Name, Email):
        self.name = Name
        self.email = Email
        self.account_balance = BankAccount(Int_rate = 0.02, Balance = 0)

    def make_deposits(self, amount):
        self.account_balance.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance.balance -= amount
        if(self.account_balance.balance < amount):
            print("Insufficiant funds: Charging a $5 fee.")
            self.account_balance.balance = self.account_balance.balance - 5
        return self

    def display_user_balance(self):
        print(self.name +"'s balance is "+ "$" + str(self.account_balance.balance))
        return self

    def transfer_money(self, other_user, amount):
        pass
        return self

Elena = User("Elena", "elena@email")
Bethany = User("Bethany", "bethany@email")
Tito = User("Tito", "tito@email")

Elena.make_deposits(100).make_deposits(100).make_deposits(100).make_withdrawal(20).display_user_balance()

Bethany.make_deposits(100).make_deposits(100).make_withdrawal(20).make_withdrawal(20).display_user_balance()

Tito.make_deposits(80).make_withdrawal(100).make_withdrawal(20).make_withdrawal(20).display_user_balance()
