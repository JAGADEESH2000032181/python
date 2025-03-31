class Person:
    def __init__(self, name = "guest"):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}"
p =Person("alice")
print(p.greet())
p2 = Person()
print(p2.greet())