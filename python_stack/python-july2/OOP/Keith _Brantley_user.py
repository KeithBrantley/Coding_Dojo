class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print('account balance is ' + str(self.balance))
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
        

# account1 = BankAccount(100)
# account2 = BankAccount(200)

# account1.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()
# print(account1.balance)

# account2.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()
# print(account2.balance)


class User:
    def __init__(self, user_name, email_address):
        self.name = user_name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(self.name + ' account balance is ' + str(self.account.balance))
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        print(f'{self.name} transfered {amount} to {other_user.name}')
        return self


guido = User('Guido Von Rossum', 'guido@gmail.com')
monty = User('Monty Python', 'monty@gmail.com')

# print(guido.name)
# print(monty.name)

guido.make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()

monty.make_deposit(100).make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()

# monty.transfer_money(guido, 100)
# guido.display_user_balance()

# monty.display_user_balance()
# guido.transfer_money(monty, 100)
# monty.display_user_balance()

# print('Guidos account balance is ' + str(guido.account_balance))

