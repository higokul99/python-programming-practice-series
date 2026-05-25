class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} started")

class Car(Vehicle):
    def drive(self):
        print("Driving the car")

class Bike(Vehicle):
    def ride(self):
        print("Riding the bike")


c = Car("Range Rover")
c.start()
c.drive()

b = Bike("RE GT 650")
b.start()
b.ride()