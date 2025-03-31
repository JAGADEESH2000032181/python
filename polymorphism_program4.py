class Calculator:
    def __init__(self,*ele):
       self.ele = ele
    def add(self):
        return sum(self.ele)
c = Calculator(2,3,4,5)
print(c.add())
