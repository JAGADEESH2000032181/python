"""Q1: Person Class
Problem: Create a Person class with attributes name and age, and a method introduce() that prints a greeting.

Input
p1 = Person("Alice", 25)
p1.introduce()

Expected Output:

Hello, my name is Alice and I am 25 years old.

"""""
class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def introduce(self):
        print(
            f"Hello, my name is {self.name} and I am {self.age} years old."
            )

p1 = Person("Alice",25)
p1.introduce()