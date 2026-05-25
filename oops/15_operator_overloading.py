class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    
n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Gokul")
print(s)

class Test:
    def add(self, a):
        print(self.a)

    def add(self, a , b):
        print(self.a + self.b)

t = Test()
t.add(10)
t.add(22,10)