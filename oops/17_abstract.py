from abc import ABC, abstractmethod
import math

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment")

class Card(Payment):
    def pay(self):
        print("Card Payment")

class Crypto(Payment):
    def pay(self):
        print("Crypto payment")
    def wallet(self):
        print("Crypto wallet")

payments = [UPI(),Card()]
for p in payments:
    p.pay()

c = Crypto()
c.wallet()

class ReportGenerator(ABC):
    @abstractmethod
    def generator(self):
        pass

class PDFReport(ReportGenerator):
    def generate(self):
        print("Generating PDF")


class ExcelReport(ReportGenerator):
    def generate(self):
        print("Generating Excel")



class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius**2)


if __name__ == "__main__":
    r = Rectangle(width=5,height=10)
    c = Circle(radius=3)

    print(f"Area of Rectangle : {r.area}")
    print(f"Area of Circle: {c.area:.2f}")