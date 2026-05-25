class Dog:
    def sound(self):
        print("bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()


class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print('Dog : barking')

d = Dog()
d.sound()