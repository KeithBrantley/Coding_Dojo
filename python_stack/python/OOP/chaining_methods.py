class User:
    def __init__(self, Name, Account_Balance):
        self.name = Name
        self.account_balance = Account_Balance

    def make_deposits(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name +"'s" + " balance is "+ "$" + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        pass
        return self

Elena = User("Elena", 0)
Bethany = User("Bethany", 0)
Tito = User("Tito", 0)

Elena.make_deposits(100).make_deposits(100).make_deposits(100).make_withdrawal(20).display_user_balance()
# Elena.make_deposits(100)
# Elena.make_deposits(100)
# Elena.make_withdrawal(20)
# Elena.display_user_balance()

Bethany.make_deposits(100).make_deposits(100).make_withdrawal(20).make_withdrawal(20).display_user_balance()
# Bethany.make_deposits(100)
# Bethany.make_withdrawal(20)
# Bethany.make_withdrawal(20)
# Bethany.display_user_balance()

Tito.make_deposits(100).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).display_user_balance()
# Tito.make_withdrawal(20)
# Tito.make_withdrawal(20)
# Tito.make_withdrawal(20)
# Tito.display_user_balance()