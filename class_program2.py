"""
Q2: Rectangle Class
Problem: Implement a Rectangle class with length and width attributes, and a method area() to compute its area.

Input

r1 = Rectangle(10, 5)
print(r1.area())

Expected Output:
50
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return (self.length)*(self.width)
r1 = Rectangle(20,30)
print(r1.area())


