class User:
    def __init__(self, name, email, balance = 0):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
    

    def make_withdrawal(self, amount):
        self.balance -= amount
 

    def display_user_balance(self):
        print(f"{self.name} balance is ${self.balance}.")


    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        print(f"{self.name} transfered ${amount} to {other_user.name}.")
        return self


Elena = User('Elena', 'elena@gmail.com', 0)
Bethany = User('Bethany', 'bethany@gmail.com', 0)
Tito = User('Tito', 'tito@gmail.com', 0)

print(Elena.email)
print(Bethany.email)
print(Tito.email)

Elena.make_deposit(100)
Elena.make_deposit(100)
Elena.make_deposit(100)
Elena.make_withdrawal(50)
Elena.display_user_balance()

Bethany.make_deposit(100)
Bethany.make_deposit(100)
Bethany.make_withdrawal(50)
Bethany.make_withdrawal(50)
Bethany.display_user_balance()

Tito.make_deposit(500)
Tito.make_withdrawal(100)
Tito.make_withdrawal(100)
Tito.make_withdrawal(100)
Tito.display_user_balance()

Elena.transfer_money(Tito, 100)
Elena.display_user_balance()
Tito.display_user_balance()