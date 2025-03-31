"""
Q10: Convert Object to String
Problem:
Create a Car class with __str__() to return a formatted string.

Input:

c = Car("Toyota", "Corolla")
print(c)
Expected Output:

Toyota Corolla
"""
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"{self.brand} {self.model}"
c = Car("Toyota","Corolla")
print(c)