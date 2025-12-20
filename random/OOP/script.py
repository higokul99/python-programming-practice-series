class Dog:
    def __init__(self, name, breed, owner):
        self.name =  name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f'[OWNER: {self.owner.name}][DOG: {self.name}: {self.breed}] : Whoof Whoof')

class Owner:
    def __init__(self, name, age, address, contact_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = contact_number

o1 = Owner("Danny",25,"122 Street","999-888-7777")

d1 = Dog("Rocky","German Shephard", o1)
d1.bark()
print(f"[OWNER: {d1.owner.name}]")


class User:
    def __init__(self, name, email):
        self.name = name
        self._email = email

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

u1 = User("Hamza","hamza@gmail.com")
print("Email address: ",u1.get_email())
set_email = u1.get_