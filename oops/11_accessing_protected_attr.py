class Parent:
    def __init__(self):
        self._money = 1000

class Child(Parent):
    def show(self):
        print(self._money)

c = Child()
c.show()