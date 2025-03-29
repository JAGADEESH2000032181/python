"""
Q3: Laptop Class
Problem: Create a Laptop class with attributes brand, model, and ram. Add a method upgrade_ram(extra_ram).

Input

laptop = Laptop("Dell", "Inspiron", 8)
laptop.upgrade_ram(8)
print(laptop.ram)

Expected Output
16
"""

class Laptop:
    def __init__(self, brand,model,ram):
        self.brand = brand
        self.model = model
        self.ram = ram
    def upgrade_ram(self,extra_ram):
        self.ram+=extra_ram
        print(self.ram)
laptop = Laptop("Dell","Inspiron",8)
laptop.upgrade_ram(8)

