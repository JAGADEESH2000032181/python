"""
🔹 Method Overriding (Runtime Polymorphism)
Q1: Animal Sounds
Problem:
Create an Animal class with a method speak(). Then, create Dog and Cat classes that override speak().

Input:

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
Expected Output:

Bark
Meow

"""

class Animal:
    def speak(self):
        return "animal class method"
class Dog(Animal):
    def speak(self):
        return "dog class method"
class Cat(Animal):
    def speak(self):
        return "cat class method"
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
