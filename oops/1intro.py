class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")

d1 = Dog("Tommy",2)
d1.bark()


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} is Meowing")

c1 = Cat("Snow Bell", 2)
c1.meow()