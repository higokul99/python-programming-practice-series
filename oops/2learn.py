class Car:
    def __init__(self, make, model):
        self.make = make #instance attribute
        self.model = model #instance attribute
        self.speed = 0 # default value

    def accelerate(self, amount):
        self.speed += amount

    def describe(self):
        return f"{self.make} {self.model} going {self.speed} km/h"
    
# Instantiation - Calling the class creates an object
car1 = Car("Toyota","Fortuner")
car2 = Car("Land Rover","Defender")

car1.accelerate(60)
print(car1.describe())

print(car2.describe())


class Demo:
    def who_am_i(self):
        print(f"Self ID: {id(self)}")

d = Demo()
print(f"d id : {id(d)}")
d.who_am_i()


class Counter:
    count = 0

    def __init__(self, name):
        Counter.count += 1
        self.name = name

c1 = Counter("C1")
c2 = Counter("C2")

print(c1.count)