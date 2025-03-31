from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "dog sounds woof"
class Cat(Animal):
    def sound(self):
        return "cat sounds meow"
d = Dog()
c = Cat()
print(d.sound())
print(c.sound())
