"""
🔹 Q1: Private Attributes
Problem:
Create a BankAccount class with a private attribute __balance. Provide methods deposit(amount) and withdraw(amount).

Input

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())
Expected Output

Balance: 1300
"""
class BankAccount:
    def __init__(self, balance =0):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient balance")
        self.__balance-=amount
    def getBalance(self):
        return f"Balance:{self.__balance}"
acc = BankAccount()
acc.deposit(10000)
acc.withdraw(5000)
print(acc.getBalance())