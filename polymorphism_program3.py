class Payment:
    def pay(self):
        pass
class Creditcard(Payment):
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        print(f"Paid {self.amount} using credit card")
class Paypal(Payment):
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print(f"Paid {self.amount} using pay pal")

c = Creditcard(100)
c.pay()
p = Paypal(100)
p.pay()