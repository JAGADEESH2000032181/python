class Product:
    def __init__(self,num):
        self.num = num
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            return Product(self.num * other)
        return NotImplemented
    def __repr__(self):
        return f"{self.num}"
p = Product(10)
p2 = p *5
print(p2)
