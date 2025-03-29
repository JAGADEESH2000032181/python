class ClassA:
    def __init__(self):
        print("Hi from clasA method")
class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        print("Hi from clasB method")
class ClassC(ClassB):
    def __init__(self):
        super().__init__()
        print("Hi from classC method")
c = ClassC()
    