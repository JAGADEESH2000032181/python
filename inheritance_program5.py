"""
 Q6: Multilevel Inheritance
Problem:
Create a three-level inheritance chain:

Animal → Mammal → Dog
Each class should print its name when instantiated.
Input

d = Dog()
Expected Output

Animal Created
Mammal Created
Dog Created
"""
class Animal:
    def __init__(self):
        print("Animal created")
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal created ")
class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("Dog created")
d = Dog()

