"""
 Q3: Calling Parent Method from Child
Problem:
Modify Q2 so that the child class calls the parent class's show() method before displaying its own message.

Input

obj = Child()
obj.show()
Expected Output

This is the parent class.
This is the child class.
"""
class Parent:
    def show(self):
        print("this is a parent class")
class Child(Parent):
    def show(self):
        super().show()
        print("this is a child class")
obj = Child()
obj.show()