"""
Problem:
Modify Q7 and swap the order of inheritance in ClassC(A, B) vs ClassC(B, A). Observe how Python resolves methods.

Input

obj = ClassC()
obj.greet()
Expected Output (depends on order)

Hello from ClassA  # If C(A, B)
OR
Hello from ClassB  # If C(B, A)
"""

class ClassA:
    def greet(self):
        print("Hello from classA")
class ClassB:
    def greet(self):
        print("hello from classB")
class ClassC(ClassB,ClassA):
    pass
c = ClassC()
c.greet()