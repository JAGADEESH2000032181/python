"""
🔹 Q2: Overriding a Method
Problem:
Create a Parent class with a method show(). Then, create a Child class that overrides the show() method.

Input
obj = Child()
obj.show()

Expected Output
This is the child class.
"""

class Parent:
    def show (self):
        print("this is a parent class")
class Child(Parent):
    def show (self):
        print("this is a child class")
child = Child()
child.show()