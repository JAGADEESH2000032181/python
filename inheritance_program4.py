"""
🔹 Q4: Constructor Overriding
Problem:
Create a Person class with attributes name and age. The Employee class should inherit from Person and also have salary. Ensure that Employee's constructor overrides Person's constructor.

Input

e = Employee("Alice", 30, 50000)
print(e.name, e.age, e.salary)
Expected Output

Alice 30 50000
"""
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name,age,salary):
        super().__init__(name,age)
        self.salary =salary
e = Employee("Alice",30,5000)
print(e.name,e.age,e.salary)
