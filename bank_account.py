
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("\n", "-"*10)
            print("\nInsufficient funds: Charging a $5 fee")
            self.balance -= 5
        if self.balance > 100:
            self.balance += self.int_rate
        return self
    def display_account_info(self):
        print("\n", "-"*10)
        print(f"\nAccount balance is: {self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.int_rate
        return self

account1 = BankAccount(0.02, 100)
account1.deposit(100).deposit(100).deposit(100).withdraw(20).display_account_info()

account2 = BankAccount(0.02, 20)
account2.deposit(50).deposit(50).withdraw(150).display_account_info()