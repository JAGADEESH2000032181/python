"""
Q5: BankAccount Class
Problem: Implement a BankAccount class where users can deposit and withdraw money. Display balance using check_balance().

Input
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.check_balance())

Expected Output
Balance: 1300
"""
class BankAccount:
    def __init__(self,balance =0):
        self.balance = balance
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        self.balance-=amount
    def check_balance(self):
        print(f"Balance :{self.balance}")
acc = BankAccount(100)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()

