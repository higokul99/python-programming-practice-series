class Animal:
    def show(self):
        print("Animal show")

class Dog(Animal):
    def show(self):
        super().show()
        print("Dog show")

class Cat(Animal):
    def show(self):
        print("Cat show")

d = Dog()
d.show()