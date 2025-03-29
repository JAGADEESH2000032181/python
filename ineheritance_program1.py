"""
🔹 Q1: Basic Inheritance
Problem:
Create a Vehicle class with attributes brand and speed. Then, create a Car class that inherits from Vehicle and has an additional attribute fuel_type.

Input

car = Car("Toyota", 120, "Petrol")
print(car.brand, car.speed, car.fuel_type)

Expected Output:
Toyota 120 Petrol
"""

class Vehicle:
    def __init__(self, brand, speed,fuel_type):
        self.brand = brand
        self.speed = speed
        self.fuel_type = fuel_type
class Car(Vehicle):
    pass
car = Car("Toyota", 120,"petrol")
print(car.brand,car.speed,car.fuel_type)




    