class Animal:
    def __init__(self):
        print("Constructor: Animal")

    def eat(self):
        print("Animal is eating")

    def sound(self):
        print("Animal: Sound Method call")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('Dog constructor')
    def bark(self):
        print("Barking")

    def sound(self):
        super().sound()
        print("Dog: Sound method call")

# Multilevel Inheritance
class Puppy(Dog):
    def eat(self):
        print("Puppy eating")

# d = Dog()
# d.eat()
# d.bark()
# d.sound()

# p = Puppy()
# p.eat()
# p.bark()


