class Parent:
    def __init__(self):
        self._secret = "hidden"


class Child(Parent):
    def show(self):
        print(self._secret)

c = Child()
c.show()


class DatabaseConnection():
    def __connect():
        pass

    def fetch_users(self):
        self.__connect() # Internal DB logic hidden

class UserService():
    def __validate_user(self):
        pass

    def create_user(self):
        self.__validate_user() # Private validation logic hidden internally

class Employee:
    def __init__(self):
        self.__id = 101

    @property
    def id(self):
        return self.__id
    
e = Employee()
print(e.id)

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h

r = Rectangle(10,20)
print(r.area)