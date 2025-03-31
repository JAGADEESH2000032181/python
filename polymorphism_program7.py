class Box:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def volume(self):
        return self.a * self.b * self.c
    def __lt__(self,other):
        if isinstance(other, Box):
            return self.volume()<other.volume()
        else:
            return NotImplemented
    def __repr__(self):
        return f"Box(BoxLength: {self.a},BoxWidth:{self.b},boxHeight:{self.c})"
b1  = Box(20,30,40)
b2 = Box(100,500,600)
print(b1>b2)
print(b1<b2)


